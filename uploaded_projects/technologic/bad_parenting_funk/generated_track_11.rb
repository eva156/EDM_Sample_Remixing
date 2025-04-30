samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\bad_parenting_funk\samples'
use_bpm 59
downbeat_count = range(0, 51, 1)
set :downbeat_time, 1.7
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 1) % 12 == 0 || (x + 2) % 13 == 0 || (x + 3) % 14 == 0 || (x + 14) % 17 == 0 || (x + 16) % 19 == 0)
			return true
		else 
			if false
				return 1
			else 
				return false
			end
		end
	else 
		x = (x - 51)
		if ((x + 5) % 9 == 0 || (x + 6) % 10 == 0 || x % 11 == 0 || (x + 8) % 11 == 0 || (x + 7) % 11 == 0 || x % 12 == 0 || (x + 6) % 14 == 0 || (x + 8) % 15 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if ((x + 1) % 12 == 0 || (x + 2) % 13 == 0 || (x + 3) % 14 == 0 || (x + 11) % 15 == 0 || (x + 4) % 15 == 0 || (x + 12) % 16 == 0 || (x + 17) % 18 == 0)
			return true
		else 
			if true
				return false
			else 
				return 0
			end
		end
	else 
		x = (x - 51)
		if (x % 8 == 0 || (x + 3) % 11 == 0 || (x + 6) % 14 == 0 || (x + 7) % 15 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		if ((x + 3) % 10 == 0 || (x + 6) % 11 == 0 || (x + 8) % 12 == 0 || (x + 12) % 13 == 0 || (x + 12) % 14 == 0 || (x + 1) % 14 == 0 || (x + 5) % 16 == 0 || (x + 7) % 17 == 0 || (x + 11) % 19 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 51)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	else 
		x = (x - 51)
		if ((x + 8) % 9 == 0 || (x + 1) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 3) % 13 == 0 || (x + 10) % 14 == 0 || (x + 12) % 16 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if x % 19 == 0
			return true
		else 
			return x > 19
		end
	else 
		x = (x - 51)
		if x % 2 == 1
			return true
		else 
			if false
				return 1
			else 
				return false
			end
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 1) % 12 == 0 || (x + 3) % 14 == 0)
			return true
		else 
			if true
				return false
			else 
				return 0
			end
		end
	else 
		x = (x - 51)
		if ((x + 3) % 4 == 0 || (x + 2) % 4 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		if ((x + 2) % 4 == 0 || (x + 1) % 4 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 51)
		if ((x + 3) % 4 == 0 || (x + 4) % 8 == 0 || (x + 1) % 9 == 0 || (x + 6) % 11 == 0)
			return false
		else 
			return 1
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	else 
		x = (x - 51)
		return false
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		if ((x + 2) % 9 == 0 || (x + 1) % 11 == 0 || (x + 8) % 12 == 0 || (x + 5) % 12 == 0 || (x + 3) % 13 == 0 || (x + 12) % 14 == 0 || (x + 1) % 14 == 0 || x % 16 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 51)
		if ((x + 2) % 6 == 0 || (x + 10) % 14 == 0 || (x + 14) % 15 == 0 || (x + 12) % 16 == 0)
			return true
		else 
			if true
				return false
			else 
				return 1
			end
		end
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		if ((x + 8) % 10 == 0 || (x + 6) % 12 == 0 || (x + 11) % 13 == 0 || (x + 4) % 13 == 0 || (x + 2) % 14 == 0)
			return false
		else 
			return 0
		end
	else 
		x = (x - 51)
		if ((x + 2) % 7 == 0 || (x + 5) % 10 == 0 || (x + 1) % 10 == 0 || (x + 10) % 11 == 0)
			return false
		else 
			return 1
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 0.537, decay: 0.628, decay_level: 0.682, sustain: 1.114, sustain_level: 0.537, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 0.395, decay: 0, decay_level: 0.395, sustain: 1.741, sustain_level: 0.395, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.053, attack_level: 0.777, decay: 0.228, decay_level: 0.89, sustain: 1.436, sustain_level: 0.818, release: 0.024 if sleep_sample_2(idx)
	sample samps, 3, start: 0.0, attack: 0.0, attack_level: 0.526, decay: 0.063, decay_level: 0.82, sustain: 1.624, sustain_level: 0.81, release: 0.055 if sleep_sample_3(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.536, decay: 0.424, decay_level: 1.0, sustain: 1.311, sustain_level: 1.0, release: 0.006 if sleep_sample_4(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.206, decay: 0.409, decay_level: 0.742, sustain: 1.267, sustain_level: 0.634, release: 0.066 if sleep_sample_5(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.426, decay: 0.052, decay_level: 0.947, sustain: 1.621, sustain_level: 0.937, release: 0.069 if sleep_sample_6(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 0.58, decay: 0.124, decay_level: 0.869, sustain: 1.615, sustain_level: 0.781, release: 0.002 if sleep_sample_7(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.39, decay: 0, decay_level: 0.39, sustain: 1.741, sustain_level: 0.39, release: 0.0 if sleep_sample_8(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.444, decay: 0.142, decay_level: 0.753, sustain: 1.6, sustain_level: 0.444, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end