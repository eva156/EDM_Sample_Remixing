samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\Wimudo\samples'
use_bpm 60
downbeat_count = range(0, 107, 1)
define :sleep_sample_0 do |x|
	if x < 27
		return x > 24
	elsif x < 47
		x = (x - 47)
		return true
	elsif x < 67
		x = (x - 67)
		return true
	elsif x < 87
		x = (x - 87)
		if ((x + 9) % 10 == 0 || (x + 7) % 13 == 0)
			return false
		else 
			return 1
		end
	else 
		x = (x - 107)
		if ((x + 9) % 10 == 0 || (x + 7) % 13 == 0)
			return false
		else 
			return 1
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 7) % 9 == 0 || (x + 1) % 12 == 0 || (x + 3) % 13 == 0 || (x + 2) % 13 == 0 || (x + 4) % 15 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 5) % 7 == 0 || (x + 4) % 7 == 0)
			return true
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
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if ((x + 8) % 9 == 0 || x % 10 == 0 || (x + 9) % 10 == 0 || (x + 1) % 10 == 0 || (x + 3) % 11 == 0)
			return false
		else 
			return 1
		end
	end
end
define :sleep_sample_10 do |x|
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
		return false
	elsif x < 87
		x = (x - 87)
		return false
	else 
		x = (x - 107)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if x >= 12
				return true
			else 
				return false
			end
		end
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x % 2 == 0
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (x + 5) % 12 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if x % 3 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if x % 2 == 1
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
		return false
	elsif x < 87
		x = (x - 87)
		return false
	else 
		x = (x - 107)
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
	end
end
define :sleep_sample_13 do |x|
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
		if ((x + 5) % 9 == 0 || (x + 1) % 11 == 0 || (x + 11) % 12 == 0 || (x + 6) % 13 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 3) % 6 == 0 || (x + 6) % 9 == 0 || (x + 3) % 9 == 0 || x % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if x >= 12
				return true
			else 
				return false
			end
		end
	end
end
define :sleep_sample_14 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 3 == 0 || x % 11 == 0)
			return true
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
	else 
		x = (x - 107)
		return false
	end
end
define :sleep_sample_15 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 67)
		if ((x + 8) % 16 == 0 || (x + 1) % 17 == 0 || (x + 2) % 18 == 0 || (x + 3) % 19 == 0 || (x + 4) % 20 == 0 || (x + 5) % 21 == 0 || (x + 6) % 22 == 0 || (x + 22) % 23 == 0 || (x + 16) % 24 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		return false
	else 
		x = (x - 107)
		if ((x + 6) % 9 == 0 || (x + 2) % 9 == 0 || (x + 10) % 11 == 0 || (x + 8) % 11 == 0 || (x + 4) % 11 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		if x % 2 == 1
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 7) % 8 == 0 || (x + 2) % 8 == 0 || (x + 6) % 9 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 7) % 8 == 0 || (x + 2) % 8 == 0 || (x + 6) % 9 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if ((x + 1) % 3 == 0 || x % 11 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x <= 1
			if true
				return true
			else 
				return false
			end
		else 
			if false
				return false
			else 
				return false
			end
		end
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if (x + 1) % 3 == 0
			return false
		else 
			return 1
		end
	else 
		x = (x - 107)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if (x + 2) % 3 == 0
			return false
		else 
			return 0
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0)
			return false
		else 
			return 0
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
	elsif x < 87
		x = (x - 87)
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
		x = (x - 107)
		if ((x + 3) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0 || (x + 4) % 11 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		return x == 0
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		return false
	else 
		x = (x - 107)
		if (x + 3) % 4 == 0
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
define :sleep_sample_6 do |x|
	if x < 27
		return x == 0
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		return false
	else 
		x = (x - 107)
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
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
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
	elsif x < 87
		x = (x - 87)
		if ((x + 3) % 6 == 0 || (x + 3) % 8 == 0 || (x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 9) % 10 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 8) % 10 == 0 || (x + 4) % 10 == 0 || x % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if (x > 0 && 32772 <= 0)
			return 17 == x
		else 
			return (true && true)
		end
	else 
		x = (x - 107)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if ((x + 7) % 9 == 0 || (x + 6) % 9 == 0 || (x + 2) % 11 == 0 || (x + 4) % 12 == 0 || (x + 8) % 14 == 0)
			return true
		else 
			return x == 5
		end
	elsif x < 87
		x = (x - 87)
		if x <= 1
			if true
				return true
			else 
				return false
			end
		else 
			if false
				return false
			else 
				return false
			end
		end
	else 
		x = (x - 107)
		return false
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 1.001, decay: 0, decay_level: 1.001, sustain: 2.02, sustain_level: 1.001, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 1.204, decay: 0, decay_level: 1.204, sustain: 2.02, sustain_level: 1.204, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_11(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_12(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_13(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 1.022, decay: 0, decay_level: 1.022, sustain: 2.02, sustain_level: 1.022, release: 0.0 if sleep_sample_14(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 1.02, decay: 0, decay_level: 1.02, sustain: 2.02, sustain_level: 1.02, release: 0.0 if sleep_sample_15(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_2(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_3(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_4(idx)
	sample samps, 11, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_5(idx)
	sample samps, 12, start: 0, attack: 0, attack_level: 1.349, decay: 0, decay_level: 1.349, sustain: 2.02, sustain_level: 1.349, release: 0.0 if sleep_sample_6(idx)
	sample samps, 13, start: 0, attack: 0, attack_level: 1.011, decay: 0, decay_level: 1.011, sustain: 2.02, sustain_level: 1.011, release: 0.0 if sleep_sample_7(idx)
	sample samps, 14, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0 if sleep_sample_8(idx)
	sample samps, 15, start: 0, attack: 0, attack_level: 1.137, decay: 0, decay_level: 1.137, sustain: 2.02, sustain_level: 1.137, release: 0.0 if sleep_sample_9(idx)
	sleep 2.0
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep 2.0
end