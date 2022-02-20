import salvar_resultados
import argumentos

from adaptive_xgboost import AdaptiveXGBoostClassifier
from adaptive_semiV2 import AdaptiveSemi
from skmultiflow.evaluation import EvaluatePrequential
from skmultiflow.data import SEAGenerator, AGRAWALGenerator
from skmultiflow.data.file_stream import FileStream
from skmultiflow.data.hyper_plane_generator import HyperplaneGenerator


# Adaptive XGBoost classifier parameters
n_estimators = 30  # Number of members in the ensemble
learning_rate = (
    0.05
    if not argumentos.HYPERPARAMETRO == "learning_rate"
    else float(argumentos.VALOR_HYPERPARAMETRO)
)  # Learning rate or eta
max_depth = (
    5
    if not argumentos.HYPERPARAMETRO == "max_depth"
    else int(argumentos.VALOR_HYPERPARAMETRO)
)  # Max depth for each tree in the ensemble
max_window_size = (
    10000
    if not argumentos.HYPERPARAMETRO == "max_window_size"
    else int(argumentos.VALOR_HYPERPARAMETRO)
)  # Max window size
min_window_size = 1  # set to activate the dynamic window strategy
detect_drift = False  # Enable/disable drift detection
ratio_unsampled = 0
small_window_size = 150

max_buffer = 25
pre_train = 15

# Criar fluxo de dados
stream = None
if argumentos.DATASET == "sea":
    stream = SEAGenerator(noise_percentage=0.1)
elif argumentos.DATASET == "hyper":
    stream = HyperplaneGenerator(noise_percentage=0.1)
elif argumentos.DATASET == "agrawal":
    stream = AGRAWALGenerator()
elif argumentos.DATASET == "airlines":
    stream = FileStream("datasets/airlines.csv")
elif argumentos.DATASET == "elec":
    stream = FileStream("datasets/elec.csv")

# Criar modelo
model = None
if argumentos.CLASSIFICADOR == "axgb":
    model = AdaptiveXGBoostClassifier(
        update_strategy="replace",
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        max_window_size=max_window_size,
        min_window_size=min_window_size,
        detect_drift=detect_drift,
        ratio_unsampled=ratio_unsampled,
    )
elif argumentos.CLASSIFICADOR == "incremental":
    model = AdaptiveSemi(
        learning_rate=learning_rate,
        max_depth=max_depth,
        max_window_size=max_window_size,
        min_window_size=min_window_size,
        ratio_unsampled=ratio_unsampled,
        small_window_size=small_window_size,
        max_buffer=max_buffer,
        pre_train=pre_train,
    )

evaluator = EvaluatePrequential(
    pretrain_size=0,
    max_samples=200000,
    # batch_size=200,
    output_file=salvar_resultados.caminho_resultado_raw,
    show_plot=False,
    metrics=["accuracy", "running_time"],
)

evaluator.evaluate(stream=stream, model=model, model_names=[argumentos.CLASSIFICADOR])

salvar_resultados.salvar()
