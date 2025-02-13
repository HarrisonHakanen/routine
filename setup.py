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
                        
    url = 'https://github.com/HarrisonHakanen/routine',
    project_urls = {
        'Código fonte': 'https://github.com/HarrisonHakanen/routine',
        'Download': 'https://github.com/HarrisonHakanen/routine/archive/refs/heads/main.zip'
    },
    license = 'MIT',
    keywords = 'routine schedule job jobs cron',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization'
    ]
)