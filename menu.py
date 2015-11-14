#!/usr/bin/env python
# encoding: utf-8

#TODO Obtencion de datos desde la clase que llama a esta (self.parent.datos  ???)
#     Pagina de avisos (4)
#     Pagina acceso rapido ( siguiente classe, ultima nota y ultima tarea)
#     Horari de 8 a 20
#     Crear pagina y botones para cada asignatura 
#     Colores?	
#     Uso: Con las teclas tab, down arrow y enter

import npyscreen, random
#npyscreen.disableColor()
class TestApp(npyscreen.NPSApp):
    def h_exit_escape(self):
	F.on_ok	
    # Metodo para crear el grid del horario
    def GridCreation(self,gd):
    	gd.values = []
        horas = [8,9,10,11,12,13,14]
        for z in range(7):
             for x in range(2):
             	row = []
             for y in range(6):
                if y == 0:
    	            row.append(horas[z])
                elif bool(random.getrandbits(1)):
                    row.append("CLASE")
                else:
                    row.append("NO CLASE")
    	     gd.values.append(row)

    def main(self):
        # Creacion del Form y de los botones de la 1a pagina
        F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
        #F.how_exited_handers[npyscreen.widget.EXITED_ESCAPE]  = self.exit_application
	fn = F.add(NotasButton, name = "Notas")
	av = F.add(AvisosButton, name = "Avisos")
        dt = F.add(HorarioButton, name = "Horario")
	lo = F.add(CSButton, name = "Cerrar session")        
        # Creacion pagina 2
        new_page_2 = F.add_page()
        t = F.add(CustomTitleText, name = "Notes:",)
        # TODO Cambiar formato del display de las notas a grid
        ms= F.add(CustomTitleSelectOne, max_height=4, value = [1,], name="RP",
                values = ["Control 1:","Control 2:","Control 3:"], scroll_exit=True)
        ms= F.add(CustomTitleSelectOne, max_height=4, value = [1,], name="PBE",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
                
        # Creacion pagina 3
    	new_page_3 = F.add_page()
    	self.GridCreation(F.add(MyGrid, columns = 6, scroll_exit=True, exit_left = True,col_titles=['','Lunes','Martes','Miercoles','Jueves','Viernes']))
        
	# Creacion pagina 4
	new_page_4 = F.add_page()

        # Metodo que se llama al seleccionar OK
        def on_ok():
            npyscreen.notify_confirm("OK Button Pressed!")
	    self.parent.stop()
        F.on_ok = on_ok
	def on_cancel():
	    F.switch_page(0)
	F.on_cancel = on_cancel
        F.edit()
 
class CustomTitleSelectOne(npyscreen.TitleSelectOne):
    how_exited = True

class CustomTitleText(npyscreen.TitleText):
    how_exited = True

# Wrap para el widget Grid
class MyGrid(npyscreen.GridColTitles):
    select_whole_line = True
    how_exited = True
    scroll_exit = True
    # Modificacion de los colores con los que se hace display el grid
    def custom_print_cell(self, actual_cell, cell_display_value):
    	if cell_display_value =='FAIL':
      		actual_cell.color = 'DANGER'
    	elif cell_display_value == 'PASS':
       		actual_cell.color = 'GOOD'
       	else:
      		actual_cell.color = 'DEFAULT'

class AvisosButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(3)
class CSButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.on_ok()
		
class NotasButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(1)

class HorarioButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(2)

	
if __name__ == "__main__":
    App = TestApp()
    App.run()
