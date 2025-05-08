samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project\EDM_Sample_Remixing\uploaded_projects\wimudo_2\samples'
use_bpm 60
downbeat_count_extracted = range(0, 107, 1)
downbeat_count_sonic = range(0, 107, 1)
set :downbeat_time, 2.0
define :sleep_sample_0 do |x|
	if x < 67
		if x == 0
			return false
		else 
			return true
		end
	elsif x < 87
		x = (x - 67)
		if ((x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 1) % 10 == 0 || (x + 5) % 12 == 0 || (x + 9) % 14 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 87)
		if ((x >= 12 && x <= 19) || x % 12 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if (x % 9 == 0 || (x + 1) % 9 == 0 || x % 16 == 0 || (x + 6) % 16 == 0)
			return false
		else 
			return true
		end
	elsif x < 47
		x = (x - 27)
		if (x >= 12 || x % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 47)
		if (x >= 12 || x % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 67)
		if ((x + 1) % 7 == 0 || (x + 3) % 8 == 0 || x % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		if (x >= 16 || x % 8 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x == 0
			return false
		else 
			return true
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
	if x < 67
		return false
	elsif x < 87
		x = (x - 67)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		return false
	end
end
define :sleep_sample_12 do |x|
	if x < 27
		if (x + 2) % 9 == 0
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 27)
		if (x % 8 == 0 || (x + 3) % 8 == 0 || (x + 9) % 11 == 0 || (x + 3) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 47)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		if x >= 12
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_13 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 27)
		if x == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 47)
		if (x >= 56 || x % 3 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_14 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		if x % 3 == 0
			return false
		else 
			return true
		end
	else 
		x = (x - 67)
		if ((x + 5) % 6 == 0 || (x + 3) % 8 == 0 || (x + 9) % 10 == 0 || (x + 3) % 10 == 0 || (x + 13) % 14 == 0 || (x + 11) % 14 == 0 || (x + 5) % 14 == 0 || (x + 4) % 19 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_15 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		if ((x >= 32 && x <= 39) || (x + 8) % 16 == 0 || (x + 1) % 17 == 0 || (x + 22) % 23 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 67)
		if 37 == x
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_2 do |x|
	if (x + 2) % 3 == 0
		return false
	else 
		return x <= 104
	end
end
define :sleep_sample_3 do |x|
	if x < 47
		return false
	else 
		x = (x - 47)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if ((x + 2) % 6 == 0 || (x + 4) % 8 == 0 || (x + 2) % 8 == 0 || x % 10 == 0 || (x + 8) % 10 == 0 || (x + 2) % 10 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 27)
		return x == 0
	elsif x < 87
		x = (x - 67)
		if (x >= 12 || x % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		if x >= 12
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 87
		if (x <= 9 || (x + 2) % 3 == 0)
			return false
		else 
			if 85 <= x
				return false
			else 
				return true
			end
		end
	else 
		x = (x - 87)
		if (x + 3) % 4 == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		if (x >= 19 || x % 19 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 27)
		return false
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		if ((x + 1) % 4 == 0 || (x + 9) % 10 == 0 || (x + 3) % 14 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 27)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 47)
		if x % 2 == 1
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 47
		false
	elsif x < 87
		x = (x - 47)
		if (x >= 34 || (x + 2) % 3 == 0 || x % 19 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 87)
		return false
	end
end
define :sleep_ambi_piano do |x|
	if x < 27
		return true
	else 
		x = (x - 27)
		return true
	end
end
define :sleep_guit_em9 do |x|
	if x < 27
		if ((x + 2) % 8 == 0 || (x + 6) % 12 == 0 || (x + 2) % 12 == 0 || (x + 14) % 16 == 0)
			return false
		else 
			return 0
		end
	elsif x < 67
		x = (x - 27)
		if ((x + 1) % 6 == 0 || (x + 7) % 8 == 0 || (x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 7) % 10 == 0 || (x + 5) % 10 == 0 || (x + 5) % 12 == 0 || (x + 2) % 19 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 67)
		if ((x + 5) % 8 == 0 || (x + 5) % 12 == 0 || (x + 1) % 12 == 0 || (x + 1) % 16 == 0 || (x + 7) % 22 == 0 || (x + 8) % 23 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_ambi_glass_hum do |x|
	if x < 27
		if ((x + 12) % 15 == 0 || (x + 4) % 15 == 0)
			return false
		else 
			return true
		end
	elsif x < 67
		x = (x - 27)
		return true
	else 
		x = (x - 67)
		if (x + 2) % 3 == 0
			return false
		else 
			return true
		end
	end
end
define :sleep_guit_e_fifths do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		return x == 0
	end
end
define :sleep_bass_voxy_c do |x|
	if x < 47
		return false
	else 
		x = (x - 47)
		if ((x + 4) % 8 == 0 || (x + 2) % 8 == 0 || (x + 8) % 10 == 0 || (x + 6) % 10 == 0 || (x + 10) % 12 == 0 || (x + 8) % 12 == 0 || (x + 6) % 12 == 0 || (x + 8) % 14 == 0 || (x + 6) % 14 == 0 || (x + 4) % 14 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_loop_mika do |x|
	if x < 67
		if (x + 1) % 3 == 0
			return false
		else 
			return 65 < x
		end
	else 
		x = (x - 67)
		if ((x + 4) % 6 == 0 || (x + 7) % 9 == 0 || (x + 4) % 9 == 0 || (x + 7) % 12 == 0 || (x + 2) % 19 == 0 || (x + 3) % 20 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_loop_drone_g_97 do |x|
	if x < 47
		if (x % 5 == 0 || (x + 3) % 5 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 47)
		if (x == 5 || 3 >= x)
			if x == 2
				return false
			else 
				return true
			end
		else 
			if x <= 38
				return false
			else 
				return true
			end
		end
	else 
		x = (x - 87)
		if x == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_loop_compus do |x|
	if x < 87
		return false
	else 
		x = (x - 87)
		return false
	end
end
define :sleep_guit_e_slide do |x|
	if x < 87
		return false
	else 
		x = (x - 87)
		return false
	end
end
define :sleep_perc_bell2 do |x|
	if x < 27
		return false
	else 
		x = (x - 107)
		if 0 < x
			return false
		else 
			return (x % 3) == 0
		end
	end
end
define :sleep_guit_harmonics do |x|
	if x < 87
		return false
	else 
		x = (x - 87)
		if ((x + 3) % 5 == 0 || (x + 2) % 5 == 0)
			return false
		else 
			return true
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count_extracted.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 0.372, decay: 0.0, decay_level: 0.882, sustain: 2.013, sustain_level: 0.928, release: 0.007 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 0.296, decay: 0.0, decay_level: 0.296, sustain: 1.955, sustain_level: 0.807, release: 0.066 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.0, attack_level: 0.091, decay: 0.003, decay_level: 0.302, sustain: 1.821, sustain_level: 0.246, release: 0.197 if sleep_sample_10(idx)
	sample samps, 3, start: 0.0, attack: 0.0, attack_level: 0.313, decay: 0.032, decay_level: 0.741, sustain: 1.987, sustain_level: 0.648, release: 0.001 if sleep_sample_11(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.118, decay: 0.367, decay_level: 0.618, sustain: 1.624, sustain_level: 0.664, release: 0.029 if sleep_sample_12(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.104, decay: 0.338, decay_level: 0.563, sustain: 1.673, sustain_level: 0.316, release: 0.01 if sleep_sample_13(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.287, decay: 0.0, decay_level: 0.287, sustain: 1.927, sustain_level: 0.709, release: 0.093 if sleep_sample_14(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 0.337, decay: 0.035, decay_level: 0.93, sustain: 1.974, sustain_level: 0.791, release: 0.011 if sleep_sample_15(idx)
	sample samps, 8, start: 0.0, attack: 0.0, attack_level: 0.309, decay: 0.948, decay_level: 0.742, sustain: 1.072, sustain_level: 0.309, release: 0.0 if sleep_sample_2(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.332, decay: 0.294, decay_level: 0.734, sustain: 1.726, sustain_level: 0.332, release: 0.0 if sleep_sample_3(idx)
	sample samps, 10, start: 0.0, attack: 0.0, attack_level: 0.052, decay: 0.033, decay_level: 0.454, sustain: 1.981, sustain_level: 0.32, release: 0.006 if sleep_sample_4(idx)
	sample samps, 11, start: 0.0, attack: 0.0, attack_level: 0.118, decay: 0.117, decay_level: 0.097, sustain: 1.888, sustain_level: 0.221, release: 0.015 if sleep_sample_5(idx)
	sample samps, 12, start: 0.0, attack: 0.0, attack_level: 0.271, decay: 0.187, decay_level: 0.116, sustain: 1.599, sustain_level: 0.054, release: 0.234 if sleep_sample_6(idx)
	sample samps, 13, start: 0.0, attack: 0.0, attack_level: 0.336, decay: 0.544, decay_level: 0.743, sustain: 1.476, sustain_level: 0.336, release: 0.0 if sleep_sample_7(idx)
	sample samps, 14, start: 0.0, attack: 0.0, attack_level: 0.158, decay: 0.038, decay_level: 0.591, sustain: 1.982, sustain_level: 0.534, release: 0.0 if sleep_sample_8(idx)
	sample samps, 15, start: 0.0, attack: 0.0, attack_level: 0.171, decay: 0.389, decay_level: 0.795, sustain: 1.631, sustain_level: 0.444, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count_sonic.tick()
	sample :ambi_piano, start: 0.0, attack: 0.398, attack_level: 0.47, decay: 0.499, decay_level: 0.379, sustain: 1.301, sustain_level: 0.0, release: 0.613 if sleep_ambi_piano(idx)
	sample :guit_em9, start: 0.0, attack: 1.439, attack_level: 0.0, decay: 1.363, decay_level: 0.0, sustain: 2.165, sustain_level: 1.03, release: 5.005 if sleep_guit_em9(idx)
	sample :ambi_glass_hum, start: 0.0, attack: 1.443, attack_level: 0.389, decay: 1.043, decay_level: 0.406, sustain: 3.116, sustain_level: 0.0, release: 4.398 if sleep_ambi_glass_hum(idx)
	sample :guit_e_fifths, start: 0.0, attack: 0.078, attack_level: 0.0, decay: 0.4, decay_level: 0.179, sustain: 0.76, sustain_level: 0.474, release: 1.884 if sleep_guit_e_fifths(idx)
	sample :bass_voxy_c, start: 0.0, attack: 0.564, attack_level: 0.102, decay: 1.274, decay_level: 0.119, sustain: 0.206, sustain_level: 0.0, release: 4.19 if sleep_bass_voxy_c(idx)
	sample :loop_mika, start: 0.0, attack: 7.335, attack_level: 0.0, decay: 0.139, decay_level: 0.372, sustain: 0.348, sustain_level: 0.388, release: 0.178 if sleep_loop_mika(idx)
	sample :loop_drone_g_97, start: 0.0, attack: 0.22, attack_level: 0.116, decay: 0.392, decay_level: 0.231, sustain: 0.666, sustain_level: 0.231, release: 0.048 if sleep_loop_drone_g_97(idx)
	sample :loop_compus, start: 0.0, attack: 0.104, attack_level: 0.372, decay: 0.374, decay_level: 0.456, sustain: 2.731, sustain_level: 0.287, release: 0.022 if sleep_loop_compus(idx)
	sample :guit_e_slide, start: 0.0, attack: 0.21, attack_level: 0.355, decay: 0.526, decay_level: 0.135, sustain: 1.247, sustain_level: 0.0, release: 2.342 if sleep_guit_e_slide(idx)
	sample :perc_bell2, start: 0.0, attack: 0.216, attack_level: 0.256, decay: 0.281, decay_level: 0.168, sustain: 0.188, sustain_level: 0.099, release: 0.432 if sleep_perc_bell2(idx)
	sample :guit_harmonics, start: 0.0, attack: 0.199, attack_level: 0.252, decay: 0.312, decay_level: 0.313, sustain: 1.295, sustain_level: 0.235, release: 0.019 if sleep_guit_harmonics(idx)
	sleep get[:downbeat_time]
end