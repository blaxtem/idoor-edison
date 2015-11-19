#!/usr/bin/env python
# encoding: utf-8

#TODO 
#     Pagina de avisos (4)
#     Pagina acceso rapido ( siguiente classe)
#     Horari de 8 a 20
#     Crear pagina y botones para cada asignatura 
#     Colores?	
#     Uso: Con las teclas tab, down arrow y enter

import npyscreen, random
#npyscreen.disableColor()
class TestApp(npyscreen.NPSApp):
    def __init__(self, parser, controller):
	    self.parser = parser
	    parser.groupCreation();
	    self.controller = controller
    def h_exit_escape(self):
	    F.on_ok	
    def main(self):
	# Creacion del Form y de los botones de la 1a pagina
        F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
        parser = self.parser
	#F.how_exited_handers[npyscreen.widget.EXITED_ESCAPE]  = self.exit_application
        F.add(npyscreen.FixedText, name = "Siguiente Clase: ", value = "Siguiente Clase: " + parser.nextClass())
        F.add(npyscreen.FixedText, name = "Ultima nota: ", value = "Ultima nota: " + parser.lastGrade())
        F.add(npyscreen.FixedText, name = "Ultima tarea: ", value = "Ultima tarea: " + parser.lastAssignment())
        F.add(CSButton, name = "Cerrar session")
	new_page = F.add_page()
	fn = F.add(NotasButton, name = "Notas")
	av = F.add(AvisosButton, name = "Avisos")
        dt = F.add(HorarioButton, name = "Horario")
	lo = F.add(CSButton, name = "Cerrar session")        
        # Creacion pagina 3
        new_page_2 = F.add_page()
        t = F.add(CustomTitleText, name = "Notes:",)
        # TODO Cambiar formato del display de las notas a grid
        for x in range(parser.numGrades()):
                F.add_widget_intelligent(npyscreen.FixedText, value = parser.grades[x][0] + ' ' + parser.grades[x][1] + ' ' + parser.grades[x][2] )
        F.add(BackButton, name = "Volver al menu principal")
        # Creacion pagina 4
    	new_page_3 = F.add_page()
    	parser.gridScheduleCreation(F.add(MyGrid, columns = 6, scroll_exit=True, exit_left = True,col_titles=['','Lunes','Martes','Miercoles','Jueves','Viernes']))
        #F.add(BackButton, name = "Volver al menu principal")
	# Creacion pagina 5
	new_page_4 = F.add_page()
	for x in range(parser.numAssignment()):
		F.add_widget_intelligent(npyscreen.FixedText, value = parser.assignments[x][0]+':'+ parser.assignments[x][1] +' para ' + parser.assignments[x][2])
        F.add(BackButton, name = "Volver al menu principal")
        # Metodo que se llama al seleccionar OK
        def on_ok():
            	npyscreen.notify_confirm("OK Button Pressed!")
	        self.controller.stop()
        F.on_ok = on_ok
	def on_cancel():
		F.switch_page(0)
	F.on_cancel = on_cancel
        F.edit()
class CustomFixedText(npyscreen.TitleSelectOne):
    how_exited = True

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
    	if cell_display_value < 5:
      		actual_cell.color = 'DANGER'
    	elif cell_display_value >= 5:
       		actual_cell.color = 'GOOD'
       	else:
      		actual_cell.color = 'DEFAULT'
class BackButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.switch_page(1)
        
class AvisosButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(4)

class CSButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.on_ok()
		
class NotasButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(2)

class HorarioButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.switch_page(3)

	
if __name__ == "__main__":
    App = TestApp()
    App.run()
