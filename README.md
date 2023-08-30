# ADFXmlTools

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">ADFXmlTools</h3>

  <p align="center">
    This project was build to fix some issues with Oracle ADF Business objects and JDeveloper.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
The project is written in Python 3. The version I have installed is 3.9
### Prerequisites

It uses standard python libraries os, re and sys. But also the lxml library that you will need to install
* pip
  ```sh
  pip install lxml
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
# checkdirectory.py
This program looks for a text file with the folderlist.txt that has the full path names of the directories that you want to check or update

if you want to update the xml files run the program as:


python .\checkdirectory.py Update or python .\checkdirectory.py u
> the program will look for duplicate Method and SortCriteria nodes an remove them.
> Renaming the original xml file with a .org extension 

If you run the program without an argument it will only check the directories without updating the xml files

In both cases a log file will be created per directory

# resetdirectory.py
> python .\resetdirectory.py

This program is used for resetting the files to their original state.

It will also read the paths from the file folderlist.txt.

In these directories it will look for files with an .org extension. Then it will check if there is .xml file with the same name.

If such a file exists it will remove the .xml file and rename the .org file to a .xml file


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





