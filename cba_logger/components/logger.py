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
	args = sys.argv[1:]

	if len(args) < 1:
		print(f"Usage: {sys.argv[0]} [Application Name Here]")
		print(f"Example: {sys.argv[0]} 'Chess Player'")
		sys.exit(1)

	max_separator_length = 30

	# noinspection PyBroadException
	try:
		if not args[1].startswith('-max_separator_length='):
			raise ValueError("Invalid argument format. Expected '-max_separator_length=<value>'.")
		v = int(args[1].split('=')[1])
		max_separator_length = v
		print(f"Using max separator length: {max_separator_length}")
	except:
		print("No max separator length provided. Using default 30.")

	application_name = args[0]
	dir = get_log_dir(application_name)
	root_separator = application_name

	logger = HoornLogger(min_level=LogType.DEBUG, outputs=[DefaultHoornLogOutput(max_separator_length=max_separator_length), FileHoornLogOutput(max_logs_to_keep=5, log_directory=Path(dir), max_separator_length=max_separator_length)], separator_root=root_separator, max_separator_length=max_separator_length)

	registration = ComponentRegistration(logger, port=50000, component_port=50001)
	registration.register_logging()