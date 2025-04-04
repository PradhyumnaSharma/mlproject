from setuptools import find_packages,setup
from typing import List

hyphen_e_dot='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this func will return list of requirements
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements=[requirement.replace("\n","") for requirement in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements



setup(

    name='mlproject',
    version= '0.0.1',
    author='Pradhyumna sharma',
    author_email='spradhyumna2@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)