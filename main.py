from mcl_python_package_template.config import get_config


def main():
    config = get_config("config.yaml")
    print(config)


if __name__ == "__main__":
    main()
