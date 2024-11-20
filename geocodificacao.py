import os
import sys
import subprocess
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import QgsApplication
from .geocodificacao_provider import GeocodificacaoProvider


class GeocodificacaoPlugin(object):

    def __init__(self):
        self.provider = None
        self.install_dependencies()

    def install_dependencies(self):
        """Installs pip and geocoder using a batch file."""
        try:
            # Path to the batch file
            batch_file = os.path.join(os.path.dirname(__file__), "install_dependencies.bat")

            # Properly quote the Python executable path
            python_executable = f'"{sys.executable}"'

            # Run the batch file
            process = subprocess.run(
                [batch_file, python_executable],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )

            # Display output to the user
            QMessageBox.information(None, "Dependency Installation", process.stdout)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(None, "Error", f"Failed to install dependencies:\n{e.stderr}")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An unexpected error occurred:\n{str(e)}")

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = GeocodificacaoProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
