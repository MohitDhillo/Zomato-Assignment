from setuptools import setup, find_packages

setup(
    name="zomato-backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "fastapi",
        "uvicorn",
        "python-dotenv",
        "psycopg2-binary"
    ],
) 