from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="btc_sent_fc_website_streamlit",
      version="1.0",
      description="streamlit web interface of btc_sent_fc",
      packages=find_packages(),
      include_package_data=True,  # includes in package files from MANIFEST.in
      install_requires=requirements)
