from setuptools import setup

setup(
    name = 'routine',
    version = '1.0.0',
    author = 'Harrison Hakanen dos Santos de Souza',
    author_email = 'harrisonhakinen@gmail.com',
    packages = ['routine'],
    
    description = 'Routine is a Python library for scheduling tasks (also known as schedules, crons, or jobs).',
    long_description = 'With Routine, you can easily configure which days a function should run, '
                        + 'set multiple executions per day, choose specific weekdays, and much more. '
                        + 'Simple and intuitive, Routine allows anyone to schedule tasks quickly and '
                        + 'efficiently—without any hassle. '
                        
    url = 'https://github.com/yanorestes/aluratemp',
    project_urls = {
        'Código fonte': 'https://github.com/yanorestes/aluratemp',
        'Download': 'https://github.com/yanorestes/aluratemp/archive/1.0.0.zip'
    }
)