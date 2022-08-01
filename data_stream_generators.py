from skmultiflow.data import (
    ConceptDriftStream,
    SEAGenerator,
    AGRAWALGenerator,
    FileStream,
    RandomRBFGeneratorDrift,
    RandomTreeGenerator,
    SineGenerator,
    STAGGERGenerator,
)
from skmultiflow.data.base_stream import Stream


def generate_sea_with_drift(
    size: int, width: int = 1, qnt_drifts=3, random_state: int = 1
):
    stream = SEAGenerator(random_state=random_state, classification_function=0)
    particoes = size / (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=SEAGenerator(
                random_state=random_state, classification_function=(i + 1) % 4
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def generate_agr_with_drift(
    size: int, width: int = 1, qnt_drifts=3, random_state: int = 1
):
    stream = AGRAWALGenerator(
        random_state=random_state, classification_function=0)
    particoes = size / (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=AGRAWALGenerator(
                random_state=random_state, classification_function=(i + 1) % 4
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def generate_randomrbf_with_drift(
    size: int, width: int = 1, qnt_drifts: int = 3, random_state: int = 1
):
    stream = RandomRBFGeneratorDrift(
        model_random_state=random_state,
        sample_random_state=random_state,
        change_speed=0.1
    )
    particoes = size // (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=RandomRBFGeneratorDrift(
                model_random_state=random_state,
                sample_random_state=random_state,
                change_speed=0.1 + 0.1 * (i + 1) % 9,
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def generate_sine_with_drift(
    size: int, width: int = 1, qnt_drifts=3, random_state: int = 1
):
    stream = SineGenerator(random_state=random_state,
                           classification_function=0)
    particoes = size / (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=SineGenerator(
                random_state=random_state + i + 1, classification_function=(i + 1) % 4
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def generate_stagger_with_drift(
    size: int, width: int = 1, qnt_drifts=3, random_state: int = 1
):
    stream = STAGGERGenerator(
        random_state=random_state, classification_function=0)
    particoes = size / (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=STAGGERGenerator(
                random_state=random_state + i + 1, classification_function=(i + 1) % 3
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def generate_randomtrees_with_drift(
    size: int, width: int = 1, qnt_drifts=3, random_state: int = 1
):
    stream = RandomTreeGenerator(
        tree_random_state=random_state, sample_random_state=random_state
    )
    particoes = size / (qnt_drifts + 1)
    for i in range(qnt_drifts):
        stream = ConceptDriftStream(
            stream=stream,
            drift_stream=RandomTreeGenerator(
                tree_random_state=random_state + i + 1,
                sample_random_state=random_state + i + 1,
            ),
            width=width,
            random_state=random_state,
            position=particoes * (i + 1),
        )
    return stream


def get_dataset(dataset: str, size: int, random_state: int, qnt_drifts: int) -> Stream:
    if dataset == "agr_a":
        return generate_agr_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "agr_g":
        return generate_agr_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "sea_a":
        return generate_sea_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "sea_g":
        return generate_sea_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "rbf_a":
        return generate_randomrbf_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "rbf_g":
        return generate_randomrbf_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "trees_a":
        return generate_randomtrees_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "trees_g":
        return generate_randomtrees_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "sine_a":
        return generate_sine_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "sine_g":
        return generate_sine_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "stagger_a":
        return generate_stagger_with_drift(
            size=size,
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "stagger_g":
        return generate_stagger_with_drift(
            size=size,
            width=int(size * 0.02),
            qnt_drifts=qnt_drifts,
            random_state=random_state,
        )
    if dataset == "higgs":
        return FileStream(f"datasets/higgs_1000000.csv", target_idx=0)
    if dataset == "hepmass":
        return FileStream(f"datasets/hepmass_all_test_1000000.csv", target_idx=0)
    if dataset == "susy":
        return FileStream(f"datasets/susy_1000000.csv", target_idx=0)
    return FileStream(f"datasets/{dataset}.csv")
