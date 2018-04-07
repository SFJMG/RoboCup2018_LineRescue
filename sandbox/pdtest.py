from devices import line_sensor_array as lsa, driver as d
from components.linedataparser import line_data_parser as ldp
from robotspecs import circumference
from components.pdcontroller import PDController as PD
from sandbox.devtools import rc, s, l, run_safe


S = 4
pd = PD(0.6, 3, 5)


def main():
	pd.reset()
	d.reset()

	while 1:
		rc.update()
		if rc.switch:
			pd.reset()
			continue

		raw = lsa.values()
		ldp.push(raw)
		if (ldp.repeat_count):
			continue
		
		pd.push((d.average_position, error_from_vector(raw)))
		
		d.set_speed(S, S * pd.value)


def m1(w):
	return d.lr(w * circumference / 4, -w * circumference / 4, 6).lr(2, 2, 6)


run_safe(main)
