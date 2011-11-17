from distutils.core import setup
 
 
setup(
    name = "django-urls-sugar",
    version = __import__("urls_sugar").__version__,
    author = "Stefano Parmesan",
    author_email = "s.parmesan@gmail.com",
    description = "A library for making complex urls in Django easier.",
    long_description = open("README.md").read(),
    license = "BSD",
    url = "http://github.com/armisael/django-urls-sugar",
    packages = [
        "urls_sugar",
    ],
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
