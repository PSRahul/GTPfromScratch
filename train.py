from omegaconf import OmegaConf
import logging

# Basic configuration for the Logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def load_dataset_to_string(config: OmegaConf) -> str:
    input_file = open(config.dataset.text_file_path)
    file_content = input_file.read()
    input_file.close()

    return file_content


def get_vocab(text_dataset: str) -> str:
    vocab = sorted(list(set(text_dataset)))
    return vocab


def main():
    config = OmegaConf.load("config/config.yaml")
    logger.info("Read file from %s", config.dataset.text_file_path)
    text_dataset = load_dataset_to_string(config)
    logger.info("Read Success")
    vocab = get_vocab(text_dataset)
    logging.info(vocab)


if __name__ == "__main__":
    main()
