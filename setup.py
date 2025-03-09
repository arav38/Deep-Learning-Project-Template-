from setuptools import setup, find_packages



def get_requriements(file_path:str)->list:
    requirment = []
    with open(file_path) as f:
        requirment = f.readlines()
        requirment = [x.replace("\n","") for x in requirment]

        if "HYPER_E_DOT" in requirment:
            requirment.remove("HYPER_E_DOT")
    return requirment

setup(
    name="x_ray"
    , version="0.1",
    author="Akshay Vilayatkar", 
    author_email="arav38vilayatkar@gmail.com",
    install_requires=get_requriements(), 
    packages=find_packages(),

)