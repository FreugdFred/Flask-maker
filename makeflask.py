import sys
sys.dont_write_bytecode = True


from text import APPTEXT, BASETEXT, HTMLTEXT, PYFILECONTENT, INITCONTENT, MakeWriteFile

import sys
import os


def main():
    SYSARGS = sys.argv[1:]
    FILENAMES = [files.lower().capitalize() for files in SYSARGS]
    CURFOLDER = os.getcwd()
    
    
    FLASKFOLDERPATH = f'{CURFOLDER}/FlaskApp'
    FLASKFOLDERPATHWEBSITE = f'{FLASKFOLDERPATH}/website'
    FLASKFOLDERPATHWEBSITESTATIC = f'{FLASKFOLDERPATHWEBSITE}/static'
    
    FLASKFOLDERPATHWEBSITESTATICSTYLES = f'{FLASKFOLDERPATHWEBSITESTATIC}/styles'
    FLASKFOLDERPATHWEBSITESTATICSCRIPTS = f'{FLASKFOLDERPATHWEBSITESTATIC}/scripts'
    FLASKFOLDERPATHWEBSITESTATICIMAGES = f'{FLASKFOLDERPATHWEBSITESTATIC}/images'

    FLASKFOLDERPATHWEBSITETEMPLATES = f'{FLASKFOLDERPATHWEBSITE}/templates'
    FLASKFOLDERPATHWEBSITECUSTOMFUCTIONS = f'{FLASKFOLDERPATHWEBSITE}/customfuctions'


    os.mkdir(FLASKFOLDERPATH)
    os.mkdir(FLASKFOLDERPATHWEBSITE)
    os.mkdir(FLASKFOLDERPATHWEBSITESTATIC)
    os.mkdir(FLASKFOLDERPATHWEBSITETEMPLATES)
    os.mkdir(FLASKFOLDERPATHWEBSITECUSTOMFUCTIONS)
    
    os.mkdir(FLASKFOLDERPATHWEBSITESTATICSTYLES)
    os.mkdir(FLASKFOLDERPATHWEBSITESTATICSCRIPTS)
    os.mkdir(FLASKFOLDERPATHWEBSITESTATICIMAGES)
    
    
    MakeWriteFile(FilePath=f'{FLASKFOLDERPATH}/app.py', FileContents=APPTEXT)
    
    
    MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITETEMPLATES}/Base.html', FileContents=BASETEXT)
    MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITESTATICSTYLES}/Base.css', FileContents='')
    MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITESTATICSCRIPTS}/Base.js', FileContents='')

    
    for FileNames in FILENAMES:
        MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITE}/{FileNames}.py', FileContents=PYFILECONTENT(FileNames))
        MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITETEMPLATES}/{FileNames}.html', FileContents=HTMLTEXT(FileNames))
        MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITESTATICSTYLES}/{FileNames}.css')
        MakeWriteFile(FilePath=f'{FLASKFOLDERPATHWEBSITESTATICSCRIPTS}/{FileNames}.js')
        
        
    with open(f'{FLASKFOLDERPATHWEBSITE}/__init__.py', 'w', encoding="UTF-8") as f:
        f.write(INITCONTENT)
        for FileNames in FILENAMES:
            f.write(f'from .{FileNames} import {FileNames.lower()}_blueprint\n')
            
        f.write(f'\n\n')

        for FileNames in FILENAMES:
            f.write(f'app.register_blueprint({FileNames.lower()}_blueprint, url_prefix="/")\n')       
        
        
    print('\033[92m\033[1mCREATED YOU FLASK APPLICATION\033[0m')
    print(f'The file path: \033[4m{FLASKFOLDERPATH}\033[0m')
    

if __name__ == "__main__":
    main()