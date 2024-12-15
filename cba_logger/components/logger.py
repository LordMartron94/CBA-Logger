import os
import sys
from pathlib import Path

from md_common_python.py_common.component_registration import ComponentRegistration
from md_common_python.py_common.logging import HoornLogger, LogType, DefaultHoornLogOutput, \
	FileHoornLogOutput


def get_log_dir(application_name: str):
	"""Gets the log directory.

	Returns:
	  The log directory.
	"""

	try:
		user_config_dir = os.path.expanduser("~")
	except Exception as e:
		raise e

	dir = os.path.join(user_config_dir, "AppData", "Local")
	log_dir = os.path.join(dir, application_name, "logs", "Components")
	return log_dir

if __name__ == "__main__":
	args = sys.argv

	if len(args) != 2:
		print(f"Usage: {args[0]} [Application Name Here]")
		print(f"Example: {args[0]} 'Chess Player'")
		sys.exit(1)

	application_name = args[1]
	dir = get_log_dir(application_name)
	root_separator = application_name

	logger = HoornLogger(min_level=LogType.DEBUG, outputs=[DefaultHoornLogOutput(), FileHoornLogOutput(max_logs_to_keep=5, log_directory=Path(dir))], separator_root=root_separator)

	registration = ComponentRegistration(logger, port=50000, component_port=50001)
	registration.register_logging()