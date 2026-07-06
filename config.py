from dataclasses import dataclass
from arguments import get_args


@dataclass
class Config:
    bank_nr: str | None
    job_nr: str | None

    def __post_init__(self):
        args = get_args()


if __name__ == "__main__":
    config = Config(bank_nr=1234, job_nr=9876)
    print(f"Bank Number: {config.bank_nr}")
    print(f"Job Number: {config.job_nr}")