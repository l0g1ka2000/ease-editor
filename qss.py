QSS = '''
QWidget{
background-color: rgb(180, 134, 159); 
    border-width: 10px;
    border-radius: 10px;
    border-color: purple;

}
QPushButton { 
    background-color: rgb(190, 90, 100); 
    border-width: 10px;
    border-radius: 10px;
    border-color: purple;
    font: 18px "Montserrat";
    min-width: 5em;
    padding: 10px;
}
QPushButton:pressed {
    background-color: pink;
    border-style: dotted;
}
QGroupBox {
    color: orange;
    font: 20px;
    border-radius: 10px;
    border: 5px purple;
    margin-top: 5ex;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}
QRadioButton {
    font: bold 20px;
}
QRadioButton::indicator {
    width: 20px;
    height: 20px;
    border-radius: 10px;
}
QRadioButton::indicator::unchecked {
    border: 4px solid; 
    border-color: blue;
    background-color: yellow;
    border-radius: 7px;
}
QRadioButton::indicator:unchecked:hover {
    border-color: yellow;
    background-color: pink;
    border-radius: 7px;
}
QLabel { 
    font: 20px "Montserrat";
}
QListWidget{
    background-color: purple;
    border: 2px solid black;
}
'''


