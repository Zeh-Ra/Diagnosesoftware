import tkinter as tk
import sys # Einlesen der Konsolenausgabe
#from filecmp import DEFAULT_IGNORES

import Diagnosesoftware_main as Diagnose

class GUI(tk.Tk):

    def __init__(self):
        super().__init__()

        #Window / Fenstereigenschaften
        self.title('Creo Diagnosesoftware')
        self.geometry("800x500") #in Pixeln
        self.config(background="#b4c6d0") #Graublau-Ton

        #Label /Textüberschrift
        self.label = tk.Label(self, text='Versionsprüfung', bg='#b4c6d0', font=('Arial', 40, 'bold'), fg='black')
        self.label.pack(padx=20, pady=20)

        #Textarea / Textfeld
        self.labeltext = tk.Text(self, height=18, width=150, font='System', bg='#E1E8EC')
        self.labeltext.pack(padx=20, pady=20) #in Pixeln
        self.labeltext.config(state=tk.DISABLED) #Zustand des Widgets Labeltext

        #Ermöglicht die Ausgabe direkt auf der Bildschirmkonsole
        self.old_stdout = sys.stdout
        sys.stdout = self

        #Button / Schaltfläche
        self.button = tk.Button(self, text='Start', height=2, width=10)
        self.button['command'] = self.button_clicked
        self.button.pack()


    #aufgerufen, wenn etwas in `print()` geschrieben wird
    #Konsolenausgabe wird im Textfeld angezeigt - Formatierung entfällt
    def write(self, message):
        #Entferne Zeilenumbrüche
        message = message.rstrip()
        self.labeltext.config(state=tk.NORMAL)  #Ermögliche das Bearbeiten des Widgets
        self.labeltext.insert(tk.END, message + "\n")  #Füge die Nachricht ein das Textfeld der Oberfläche
        self.labeltext.config(state=tk.DISABLED)  #Setze es wieder auf Read-Only / nicht bearbeitbar
        self.labeltext.yview(tk.END)  #Scrollt nach unten, um die neueste Nachricht anzuzeigen

    def flush(self):
        pass  #Notwendig, aber wird nicht gebraucht, da wir keine Ausgabe puffern müssen.

    #Durch klicken des Buttons wird eine Instanz der Klasse Diagnose in der Datei Diagnosesoftware_main.py erstellt
    def button_clicked(self):
        #Orginal Konfigurationsfile
        #dir_test = r'U:\zcelik\AP_Projektprüfung_Diagnosesoftware\Konfigurationsdatei\Creo_Konfig_Vfinal.json'
        #Test files
        dir_test = r'U:\zcelik\AP_Projektprüfung_Diagnosesoftware\Konfigurationsdatei\Creo_Konfig_V2.json'
        #dir_test = r'U:\zcelik\AP_Projektprüfung_Diagnosesoftware\Konfigurationsdatei\Creo_Konfig_Vfinaltest.json'
        Software = Diagnose.Diagnose(dir_test)
        #Software.start_prozess() #Wird durch den Konstruktor ausgeführt


if __name__ == "__main__":
    app = GUI()
    app.mainloop()