samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\technologic\samples'
use_bpm 63
downbeat_count = range(0, 150, 1)
set :downbeat_time, 1.88
define :sleep_sample_0 do |x|
	if ((x + 9) % 10 == 0 || (x + 8) % 10 == 0 || (x + 7) % 20 == 0 || (x + 27) % 30 == 0 || (x + 17) % 30 == 0)
		return false
	else 
		if (23 == x || 83 == x)
			return false
		else 
			if 140 == x
				return false
			else 
				return 1
			end
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 67)
		return false
	else 
		x = (x - 150)
		if (x + 5) % 8 == 0
			return true
		else 
			if (x == 1 || 77 < x)
				if x % 4 == 0
					return false
				else 
					return true
				end
			else 
				if 76 == x
					return true
				else 
					return false
				end
			end
		end
	end
end

define :sleep_sample_2 do |x|
	if x < 27
		return false
	else 
		x = (x - 150)
		if x == 0
			return true
		else 
			return false
		end
	end
end

define :sleep_sample_7 do |x|
	if x < 47
		if (x + 4) % 5 == 0
			return false
		else 
			return true
		end
	elsif x < 107
		x = (x - 107)
		return false
	else 
		x = (x - 150)
		if ((x + 5) % 8 == 0 || (x + 1) % 20 == 0)
			return true
		else 
			if (x <= 34 || 37 == x)
				return 1 == x
			else 
				if x % 8 == 0
					return false
				else 
					return true
				end
			end
		end
	end
end
define :sleep_sample_13 do |x|
	if x < 127
		if ((x + 5) % 12 == 0 || (x + 2) % 12 == 0 || (x + 8) % 15 == 0 || (x + 5) % 15 == 0 || (x + 2) % 15 == 0 || (x + 11) % 18 == 0 || (x + 8) % 18 == 0 || (x + 14) % 21 == 0 || (x + 8) % 21 == 0 || (x + 11) % 24 == 0 || (x + 8) % 24 == 0)
			return false
		else 
			if not(126 == x)
				if 2 == x
					return false
				else 
					return true
				end
			else 
				return false
			end
		end
	else 
		x = (x - 150)
		return false
	end
end

define :sleep_sample_3 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if x == 0
			if true
				return true
			else 
				return 1
			end
		else 
			if true
				return false
			else 
				return 1
			end
		end
	else 
		x = (x - 150)
		return false
	end
end

define :sleep_ambi_lunar_land do |x|
	if x < 47
		if (x % 11 == 0 || (x + 1) % 11 == 0 || (x + 6) % 19 == 0 || (x + 20) % 21 == 0 || (x + 9) % 22 == 0)
			return true
		else 
			if (46 == x || 3 == x)
				if x == 0
					if false
						return false
					else 
						return false
					end
				else 
					return true
				end
			else 
				return x == 24
			end
		end
	elsif x < 107
		x = (x - 107)
		if (x % 4 == 0 || x % 6 == 0 || (x + 4) % 6 == 0 || (x + 2) % 8 == 0 || x % 10 == 0 || (x + 6) % 10 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_perc_till do |x|
	if x < 47
		return false
	elsif x < 107
		x = (x - 107)
		return false
	else 
		x = (x - 150)
		if x == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_loop_mika do |x|
	if x < 27
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if (x + 2) % 4 == 0
			return false
		else 
			if x >= 74
				return false
			else 
				return 1
			end
		end
	else 
		x = (x - 150)
		if (x % 19 == 0 || (x + 10) % 19 == 0 || (x + 5) % 19 == 0)
			return true
		else 
			return (4 == x || 23 == x)
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.464, decay_level: 0.634, sustain: 1.29, sustain_level: 0.557, release: 0.161 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 0.476, decay: 0.011, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.028 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.0, attack_level: 0.65, decay: 0.463, decay_level: 0.278, sustain: 1.453, sustain_level: 1.0, release: 0.0 if sleep_sample_2(idx)
	sample samps, 3, start: 0.0, attack: 0.227, attack_level: 0.911, decay: 0.304, decay_level: 0.351, sustain: 1.358, sustain_level: 1.0, release: 0.026 if sleep_sample_7(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.246, decay: 0.026, decay_level: 1.0, sustain: 1.853, sustain_level: 1.0, release: 0.036 if sleep_sample_13(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.368, decay: 0.003, decay_level: 1.0, sustain: 1.892, sustain_level: 1.0, release: 0.021 if sleep_sample_3(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sample :ambi_lunar_land, start: 0.0, attack: 1, attack_level: 1.155, decay: 0.684, decay_level: 1.33, sustain: 5.633, sustain_level: 1.232, release: 0.0 if sleep_ambi_lunar_land(idx)
	sample :perc_till, start: 0.0, attack: 0.055, attack_level: 1.423, decay: 0.333, decay_level: 1.222, sustain: 2.272, sustain_level: 1.165, release: 0.006 if sleep_perc_till(idx)
	sample :loop_mika, start: 0.0, attack: 0.0, attack_level: 1.366, decay: 0.608, decay_level: 1.294, sustain: 0.212, sustain_level: 0.0, release: 7.18 if sleep_loop_mika(idx)
	sleep get[:downbeat_time]
end