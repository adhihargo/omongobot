export PATH:=E:\prog\venv_omongobot\Scripts;$(PATH)

all: ui

ui: ../app_lib/forms/ui_main_window.py \
	../app_lib/forms/ui_dialog_preferences.py \
	../app_lib/forms/ui_dialog_record.py

../app_lib/forms/ui_%.py: %.ui
	pyside2-uic.exe $< -o $@
