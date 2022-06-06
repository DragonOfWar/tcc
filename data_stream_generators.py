from skmultiflow.data import (
    ConceptDriftStream,
    SEAGenerator,
    AGRAWALGenerator,
    FileStream,
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
    stream = AGRAWALGenerator(random_state=random_state, classification_function=0)
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
    return FileStream(f"datasets/{dataset}.csv")
