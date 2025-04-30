samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\vois_sur_ton\samples'
use_bpm 58
downbeat_count = range(0, 81, 1)
set :downbeat_time, 1.79
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 1) % 7 == 0 || (x + 2) % 8 == 0 || (x + 1) % 8 == 0 || (x + 2) % 11 == 0 || (x + 4) % 12 == 0 || (x + 3) % 12 == 0 || (x + 1) % 17 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 5 == 0 || (x + 5) % 11 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (0 < x && (true && true))
			if 3 <= x
				return false
			else 
				return true
			end
		else 
			if 66 == x
				if true
					return false
				else 
					return false
				end
			else 
				return false
			end
		end
	else 
		x = (x - 81)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 9 == 0 || (x + 8) % 10 == 0 || (x + 6) % 12 == 0 || (x + 7) % 13 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if not(18 >= x)
				if not(true)
					if false
						return false
					else 
						return false
					end
				else 
					return false
				end
			else 
				if 15 < x
					return true
				else 
					return false
				end
			end
		end
	else 
		x = (x - 81)
		if x % 2 == 1
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if ((x + 3) % 6 == 0 || (x + 2) % 6 == 0 || x % 10 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if ((false || false) || 4 < x)
				if 1 == 0
					if false
						return false
					else 
						return false
					end
				else 
					if false
						return false
					else 
						return 0
					end
				end
			else 
				if x % 8 == 0
					return 0
				else 
					if true
						return false
					else 
						return false
					end
				end
			end
		end
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		if ((x + 3) % 6 == 0 || (x + 6) % 9 == 0 || (x + 3) % 9 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 4 == 0 || x % 11 == 0)
			return false
		else 
			return 0
		end
	else 
		x = (x - 81)
		if (x + 1) % 3 == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_12 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 8 == 0 || (x + 9) % 10 == 0 || (x + 7) % 10 == 0 || (x + 2) % 11 == 0 || (x + 6) % 13 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if x >= 12
				return true
			else 
				return false
			end
		end
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if x > 5
				if false
					return false
				else 
					return 1
				end
			else 
				return false
			end
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
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
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if ((false || false) || 4 < x)
				if 1 == 0
					if false
						return false
					else 
						return false
					end
				else 
					if false
						return false
					else 
						return 0
					end
				end
			else 
				if x % 8 == 0
					return 0
				else 
					if true
						return false
					else 
						return false
					end
				end
			end
		end
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return x == 0
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if x > 5
				if false
					return false
				else 
					return 1
				end
			else 
				return false
			end
		end
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if x % 2 == 1
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 8 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 81)
		return false
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 10) % 11 == 0 || (x + 6) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		return false
	else 
		x = (x - 81)
		if ((x + 2) % 8 == 0 || (x + 8) % 9 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_6 do |x|
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
	elsif x < 47
		x = (x - 47)
		if x % 3 == 0
			return false
		else 
			return 0
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 81)
		if ((x + 4) % 5 == 0 || (x + 6) % 7 == 0 || (x + 1) % 8 == 0 || (x + 8) % 9 == 0)
			return true
		else 
			return 12 == x
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		if (x % 4 == 0 || x % 6 == 0 || (x + 2) % 6 == 0 || (x + 2) % 8 == 0 || (x + 8) % 10 == 0)
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if (x % 8 == 0 || (x + 7) % 9 == 0 || (x + 6) % 11 == 0)
			return false
		else 
			return 0
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 5 == 0 || (x + 5) % 11 == 0 || (x + 6) % 12 == 0 || (x + 7) % 13 == 0)
			return false
		else 
			if false
				return 0
			else 
				return 0
			end
		end
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if x > 5
				if false
					return false
				else 
					return 1
				end
			else 
				return false
			end
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	else 
		x = (x - 81)
		if (x + 4) % 9 == 0
			return false
		else 
			if ((false || false) || 4 < x)
				if 1 == 0
					if false
						return false
					else 
						return false
					end
				else 
					if false
						return false
					else 
						return 0
					end
				end
			else 
				if x % 8 == 0
					return 0
				else 
					if true
						return false
					else 
						return false
					end
				end
			end
		end
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 8 == 0 || (x + 5) % 9 == 0 || (x + 4) % 9 == 0 || (x + 5) % 10 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 6 == 0 || (x + 3) % 6 == 0 || (x + 2) % 6 == 0)
			return false
		else 
			return 1
		end
	else 
		x = (x - 81)
		if (x + 2) % 3 == 0
			return false
		else 
			return true
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 0.471, decay: 0.0, decay_level: 1.0, sustain: 1.836, sustain_level: 1.0, release: 0.022 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 0.502, decay: 0.0, decay_level: 1.0, sustain: 1.824, sustain_level: 1.0, release: 0.033 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.408, decay: 0, decay_level: 0.408, sustain: 1.858, sustain_level: 0.408, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.503, decay: 0, decay_level: 0.503, sustain: 1.858, sustain_level: 0.503, release: 0.0 if sleep_sample_11(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.516, decay: 0.032, decay_level: 0.882, sustain: 1.8, sustain_level: 0.882, release: 0.026 if sleep_sample_12(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.448, decay: 0.021, decay_level: 0.799, sustain: 1.817, sustain_level: 0.881, release: 0.021 if sleep_sample_2(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.423, decay: 0.024, decay_level: 0.836, sustain: 1.801, sustain_level: 0.877, release: 0.032 if sleep_sample_3(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 0.212, decay: 0.032, decay_level: 1.0, sustain: 1.769, sustain_level: 0.975, release: 0.056 if sleep_sample_4(idx)
	sample samps, 8, start: 0.0, attack: 0.0, attack_level: 0.488, decay: 0.024, decay_level: 0.905, sustain: 1.8, sustain_level: 1.0, release: 0.033 if sleep_sample_5(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.441, decay: 0.021, decay_level: 0.838, sustain: 1.796, sustain_level: 0.848, release: 0.041 if sleep_sample_6(idx)
	sample samps, 10, start: 0.0, attack: 0.0, attack_level: 0.487, decay: 0.012, decay_level: 0.925, sustain: 1.817, sustain_level: 0.91, release: 0.029 if sleep_sample_7(idx)
	sample samps, 11, start: 0.0, attack: 0.0, attack_level: 0.351, decay: 0.021, decay_level: 0.934, sustain: 1.801, sustain_level: 0.898, release: 0.036 if sleep_sample_8(idx)
	sample samps, 12, start: 0.0, attack: 0.0, attack_level: 0.298, decay: 0.045, decay_level: 0.613, sustain: 1.713, sustain_level: 0.454, release: 0.1 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end