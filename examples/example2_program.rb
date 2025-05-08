samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project\EDM_Sample_Remixing\uploaded_projects\technologic\samples'
use_bpm 63
downbeat_count_extracted = range(0, 150, 1)
downbeat_count_sonic = range(0, 150, 1)
set :downbeat_time, 1.88
define :sleep_sample_0 do |x|
	if x < 27
		return false
	end
	if (x % 10 == 0 || (x + 2) % 10 == 0 || (x + 1) % 20 == 0 || (x + 21) % 30 == 0 || (x + 11) % 30 == 0)
		return false
	else 
		if (89 == x)
			return false
		else 
			if 29 == x
				return false
			else 
				return true
			end
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 47)
		return false
	else 
		x = (x - 67)
		if (x + 5) % 8 == 0
			return true
		else 
			if (77 == x || 76 > x)
				if 1 == x
					return true
				else 
					return false
				end
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
define :sleep_sample_10 do |x|
	if x < 47
		if (x % 27 == 0 && x != 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 47)
		if ((x + 3) % 6 == 0 || (x + 3) % 8 == 0 || (x + 1) % 8 == 0 || (x + 9) % 10 == 0)
			return false
		else 
			return true
		end
	elsif x < 127
		x = (x - 67)
		if (x >= 55 || (x + 4) % 7 == 0 || (x + 9) % 14 == 0 || (x + 16) % 21 == 0 || (x + 2) % 21 == 0 || (x + 22) % 23 == 0 || (x + 14) % 26 == 0 || (x + 1) % 27 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_11 do |x|
	if x < 127
		return false
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_12 do |x|
	if x < 67
		return false
	elsif x < 87
		x = (x - 67)
		if x >= 12
			return (x % 2) == 0
		else 
			return false
		end
	elsif x < 127
		x = (x - 87)
		return false
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_13 do |x|
	if x < 127
		if x >= 79
			return (x % 2) == 1
		end
		if ((x + 5) % 12 == 0 || (x + 2) % 12 == 0 || (x + 8) % 15 == 0 || (x + 5) % 15 == 0 || (x + 2) % 15 == 0 || (x + 11) % 18 == 0 || (x + 8) % 18 == 0 || (x + 14) % 21 == 0 || (x + 8) % 21 == 0 || (x + 11) % 24 == 0 || (x + 8) % 24 == 0)
			return false
		else 
			if (126 == x || not(true))
				return false
			else 
				if x == 2
					return false
				else 
					return true
				end
			end
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_14 do |x|
	if x < 127
		if ((x - 2) % 15 == 0 || x == 2)
			return true
		else
			if (x == 7 || x == 10 || x == 13)
				return true
			else
				return false
			end
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_15 do |x|
	if x < 27
		if x >= 20
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 27)
		if (x + 1) % 3 == 0
			return false
		else 
			return true
		end
	else 
		x = (x - 67)
		return false
	end
end
define :sleep_sample_16 do |x|
	if x < 27
		return false
	elsif x < 87
		x = (x - 27)
		return not(x == 0)
	elsif x < 107
		x = (x - 87)
		return false
	elsif x < 127
		x = (x - 107)
		return false
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_17 do |x|
	if x < 27
		if ((x + 1) % 3 == 0 || x % 14 == 0) && x != 0
			return false
		else 
			return false
		end
	elsif x < 67
		x = (x - 27)
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 67)
		if (x % 6 == 0 || (x + 4) % 8 == 0 || (x + 2) % 8 == 0 || (x + 6) % 10 == 0 || (x + 4) % 10 == 0 || (x + 2) % 10 == 0 || (x + 10) % 12 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0 || (x + 6) % 16 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_18 do |x|
	if ((x + 4) % 12 == 0 || (x + 10) % 18 == 0 || (x + 7) % 18 == 0 || (x + 4) % 18 == 0 || (x + 13) % 21 == 0 || (x + 10) % 21 == 0 || (x + 7) % 21 == 0 || (x + 13) % 24 == 0 || (x + 10) % 24 == 0 || (x + 7) % 24 == 0 || (x + 10) % 27 == 0 || (x + 4) % 27 == 0)
		return false
	else 
		if (142 == x)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_19 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		return false
	elsif x < 87
		x = (x - 67)
		return false
	elsif x < 127
		x = (x - 87)
		return false
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 67
		return false
	elsif x < 107
		x = (x - 67)
		if ((x + 8) % 16 == 0 || (x + 1) % 17 == 0 || (x + 2) % 18 == 0 || (x + 4) % 20 == 0 || (x + 5) % 21 == 0 || (x + 6) % 22 == 0 || (x + 22) % 23 == 0 || (x + 16) % 24 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		return x == 0
	end
end
define :sleep_sample_5 do |x|
	if x < 47
		return false
	else 
		x = (x - 47)
		return false
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 27)
		if ((x + 2) % 7 == 0 || (x + 10) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 47)
		if x % 2 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 67)
		if (x + 1) % 10 == 0
			return true
		else 
			if x < 1
				return true
			else 
				return false
			end
		end
	elsif x < 107
		x = (x - 87)
		if x % 2 == 1
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
define :sleep_sample_7 do |x|
	if x < 47
		if (x + 4) % 5 == 0
			return true
		else 
			false
		end
	elsif x < 107
		x = (x - 47)
		return false
	else 
		x = (x - 107)
		if ((x + 5) % 8 == 0 || (x + 1) % 20 == 0 || (x + 3) % 22 == 0 || (x + 4) % 23 == 0 || (x + 14) % 25 == 0 || (x + 25) % 26 == 0 || (x + 16) % 27 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 47
		if (x <= 15 || (x >= 21 && x <= 28) || (x >= 34 && x <= 41) || x % 12 == 0 || (x + 11) % 12 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 47)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 47)
		if ((x >= 4 && x <= 19) || (x + 4) % 8 == 0 || (x + 10) % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 67)
		return false
	end
end
define :sleep_ambi_sauna do |x|
	if x < 27
		if (x + 3) % 4 == 0
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 27)
		if x == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 47)
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 87)
		if (x % 4 == 0 || x % 6 == 0 || (x + 2) % 6 == 0 || (x + 6) % 8 == 0 || (x + 6) % 10 == 0 || (x + 2) % 10 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_perc_till do |x|
	if x < 67
		if ((x + 5) % 8 == 0 || (x + 4) % 8 == 0)
			return true
		else 
			if x == 0
				return true
			else 
				return false
			end
		end
	elsif x < 107
		x = (x - 67)
		if x % 5 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if ((x + 2) % 8 == 0 || (x + 6) % 12 == 0 || (x + 2) % 12 == 0 || (x + 6) % 16 == 0 || (x + 20) % 21 == 0 || x % 22 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_loop_mika do |x|
	if x < 127
		if x % 8 == 0
			return true
		else 
			return 124 == x
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_loop_garzul do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 27)
		return false
	else 
		x = (x - 47)
		return x == 0
	end
end
define :sleep_guit_e_slide do |x|
	if x < 87
		if x == 0
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 87)
		return x == 0
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_bass_voxy_c do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		return false
	elsif x < 127
		x = (x - 67)
		return x == 0
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_perc_bell2 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 47)
		if x == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 67)
		return false
	end
end
define :sleep_drum_splash_hard do |x|
	if x < 27
		return x == 0
	elsif x < 107
		x = (x - 27)
		return false
	else 
		x = (x - 107)
		return false
	end
end
define :sleep_loop_weirdo do |x|
	if x < 107
		return false
	elsif x < 127
		x = (x - 107)
		if x == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_ambi_dark_woosh do |x|
	if x < 27
		return x == 0
	elsif x < 87
		x = (x - 27)
		return false
	elsif x < 127
		x = (x - 87)
		return x == 0
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_glitch_bass_g do |x|
	if x < 107
		if (x + 5) % 7 == 0
			return true
		else 
			return x == 0
		end
	else 
		x = (x - 107)
		if (x % 12 == 0 || x % 18 == 0 || (x + 6) % 18 == 0 || (x + 5) % 23 == 0 || (x + 18) % 24 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_loop_drone_g_97 do |x|
	if x < 27
		return false
	elsif x < 107
		x = (x - 27)
		return false
	else 
		x = (x - 107)
		return x == 0
	end
end
define :sleep_vinyl_rewind do |x|
	if x < 27
		return x == 0
	elsif x < 47
		x = (x - 27)
		if (x + 1) % 3 == 0
			return false
		else 
			return true
		end
	elsif x < 107
		x = (x - 47)
		return x == 0
	else 
		x = (x - 107)
		if (x % 4 == 0 || (x + 1) % 4 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_vinyl_hiss do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 27)
		if (x % 4 == 0 || (x + 3) % 4 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 47)
		if (x + 3) % 6 == 0
			return true
		else 
			if x == 0
				return true
			else 
				return false
			end
		end
	else 
		x = (x - 107)
		if ((x + 1) % 12 == 0 || (x + 7) % 18 == 0 || (x + 1) % 18 == 0 || x % 23 == 0 || (x + 6) % 23 == 0 || (x + 19) % 24 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_elec_chime do |x|
	if x < 47
		if ((x + 1) % 8 == 0 || x % 31 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 47)
		if ((x + 6) % 9 == 0 || x % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 67)
		if x % 4 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 107)
		if (x % 4 == 0 || (x + 4) % 6 == 0 || (x + 2) % 6 == 0 || (x + 2) % 8 == 0 || (x + 2) % 10 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_ambi_drone do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 67)
		return false
	end
end
define :sleep_ambi_choir do |x|
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
		return x == 0
	end
end
define :sleep_bass_drop_c do |x|
	if x < 27
		return false
	elsif x < 87
		x = (x - 27)
		return false
	elsif x < 107
		x = (x - 87)
		return false
	else 
		x = (x - 107)
		return false
	end
end
define :sleep_loop_breakbeat do |x|
	if x < 47
		return false
	elsif x < 87
		x = (x - 47)
		return false
	else 
		x = (x - 87)
		return x == 0
	end
end
define :sleep_mehackit_phone3 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 27)
		return false
	elsif x < 107
		x = (x - 67)
		return false
	elsif x < 127
		x = (x - 107)
		return false
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_drum_cymbal_hard do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 47)
		if (x >= 12 || x % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 67)
		if (x + 5) % 8 == 0
			return true
		else 
			if 0 == x
				return true
			else 
				return false
			end
		end
	else 
		x = (x - 127)
		return false
	end
end
define :sleep_elec_filt_snare do |x|
	if x < 47
		if (x % 8 == 0 || (x + 1) % 8 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 47)
		return false
	elsif x < 127
		x = (x - 67)
		if ((x + 20) % 28 == 0 || (x + 12) % 28 == 0 || (x + 4) % 28 == 0)
			return true
		else 
			if not(x == 0)
				if x == 32
					return true
				else 
					return false
				end
			else 
				return 40962 <= 49169
			end
		end
	else 
		x = (x - 127)
		return x == 0
	end
end
live_loop :extracted_samples do
	idx = downbeat_count_extracted.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.464, decay_level: 0.95, sustain: 1.29, sustain_level: 0.9, release: 0.161 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 1.476, decay: 0.011, decay_level: 1.3, sustain: 1.877, sustain_level: 1.0, release: 0.028 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.0, attack_level: 0.234, decay: 0.024, decay_level: 1.0, sustain: 1.88, sustain_level: 1.0, release: 0.012 if sleep_sample_10(idx)
	sample samps, 3, start: 0.0, attack: 0.0, attack_level: 0.19, decay: 0.026, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.012 if sleep_sample_11(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.186, decay: 0.0, decay_level: 1.0, sustain: 1.873, sustain_level: 1.0, release: 0.042 if sleep_sample_12(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.246, decay: 0.026, decay_level: 0.6, sustain: 1.853, sustain_level: 0.6, release: 0.036 if sleep_sample_13(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.21, decay: 0.012, decay_level: 1.0, sustain: 1.892, sustain_level: 1.0, release: 0.012 if sleep_sample_14(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 2.436, decay: 0.007, decay_level: 2.5, sustain: 1.852, sustain_level: 2.5, release: 0.057 if sleep_sample_15(idx)
	sample samps, 8, start: 0.0, attack: 0.0, attack_level: 0.122, decay: 0.0, decay_level: 1.0, sustain: 1.897, sustain_level: 1.0, release: 0.019 if sleep_sample_16(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.183, decay: 0.0, decay_level: 1.0, sustain: 1.897, sustain_level: 1.0, release: 0.019 if sleep_sample_17(idx)
	sample samps, 10, start: 0.0, attack: 0.0, attack_level: 0.506, decay: 0.012, decay_level: 1.083, sustain: 1.859, sustain_level: 1.027, release: 0.045 if sleep_sample_18(idx)
	sample samps, 11, start: 0.0, attack: 0.0, attack_level: 0.285, decay: 0.012, decay_level: 0.944, sustain: 1.855, sustain_level: 1.0, release: 0.049 if sleep_sample_19(idx)
	sample samps, 12, start: 0.0, attack: 0.0, attack_level: 1.05, decay: 0.463, decay_level: 0.978, sustain: 1.453, sustain_level: 1.0, release: 0.0 if sleep_sample_2(idx)
	sample samps, 13, start: 0.0, attack: 0.0, attack_level: 0.368, decay: 0.003, decay_level: 1.0, sustain: 1.892, sustain_level: 1.0, release: 0.021 if sleep_sample_3(idx)
	sample samps, 14, start: 0.0, attack: 0.0, attack_level: 0.378, decay: 0.0, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.038 if sleep_sample_4(idx)
	sample samps, 15, start: 0.0, attack: 0.0, attack_level: 1.366, decay: 0.015, decay_level: 1.0, sustain: 1.856, sustain_level: 1.0, release: 0.045 if sleep_sample_5(idx)
	sample samps, 16, start: 0.0, attack: 0.0, attack_level: 0.372, decay: 0.0, decay_level: 1.0, sustain: 1.889, sustain_level: 1.0, release: 0.026 if sleep_sample_6(idx)
	sample samps, 17, start: 0.0, attack: 0.239, attack_level: 0.267, decay: 0.292, decay_level: 0.351, sustain: 1.358, sustain_level: 0.8, release: 0.026 if sleep_sample_7(idx)
	sample samps, 18, start: 0.0, attack: 0.0, attack_level: 1.5, decay: 0.001, decay_level: 1.5, sustain: 1.875, sustain_level: 1.5, release: 0.04 if sleep_sample_8(idx)
	sample samps, 19, start: 0.0, attack: 0.0, attack_level: 2.346, decay: 0.0, decay_level: 2.3, sustain: 1.88, sustain_level: 2.3, release: 0.036 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count_sonic.tick()
	sample :ambi_sauna, start: 0.0, attack: 0.23, attack_level: 0.575, decay: 0.255, decay_level: 0.557, sustain: 0.22, sustain_level: 0.0, release: 0.273 if sleep_ambi_sauna(idx)
	sample :perc_till, start: 0.0, attack: 0.178, attack_level: 0.456, decay: 0.161, decay_level: 0.389, sustain: 0.968, sustain_level: 0.0, release: 1.358 if sleep_perc_till(idx)
	#sample :loop_mika, start: 0.0, attack: 1.001, attack_level: 0.71, decay: 0.756, decay_level: 0.591, sustain: 0.504, sustain_level: 0.0, release: 5.739 if sleep_loop_mika(idx)
	sample :loop_garzul, start: 0.0, attack: 0.133, attack_level: 0.355, decay: 0.578, decay_level: 0.389, sustain: 1.811, sustain_level: 0.49, release: 5.477 if sleep_loop_garzul(idx)
	sample :guit_e_slide, start: 0.0, attack: 0.186, attack_level: 0.541, decay: 0.295, decay_level: 0.0, sustain: 0.23, sustain_level: 0.0, release: 0.072 if sleep_guit_e_slide(idx)
	sample :bass_voxy_c, start: 0.0, attack: 0.386, attack_level: 0.676, decay: 0.451, decay_level: 0.406, sustain: 2.282, sustain_level: 0.372, release: 0.026 if sleep_bass_voxy_c(idx)
	sample :perc_bell2, start: 0.0, attack: 0.019, attack_level: 0.524, decay: 1.38, decay_level: 0.423, sustain: 0.165, sustain_level: 0.0, release: 3.89 if sleep_perc_bell2(idx)
	sample :drum_splash_hard, start: 0.0, attack: 0.025, attack_level: 0.558, decay: 0.33, decay_level: 0.608, sustain: 0.772, sustain_level: 0.0, release: 1.469 if sleep_drum_splash_hard(idx)
	sample :loop_weirdo, start: 0.612, attack: 1.641, attack_level: 0.656, decay: 0.175, decay_level: 0.62, sustain: 2.513, sustain_level: 0.724, release: 0.007 if sleep_loop_weirdo(idx)
	sample :ambi_dark_woosh, start: 0.0, attack: 0.564, attack_level: 0.203, decay: 0.597, decay_level: 0.524, sustain: 1.088, sustain_level: 0.338, release: 1.454 if sleep_ambi_dark_woosh(idx)
	sample :glitch_bass_g, start: 0.0, attack: 0.0, attack_level: 0.845, decay: 0.067, decay_level: 0.862, sustain: 1.442, sustain_level: 0.0, release: 0.421 if sleep_glitch_bass_g(idx)
	sample :loop_drone_g_97, start: 0.0, attack: 0.058, attack_level: 0.423, decay: 1.266, decay_level: 0.186, sustain: 3.59, sustain_level: 0.422, release: 0.034 if sleep_loop_drone_g_97(idx)
	sample :vinyl_rewind, start: 0.0, attack: 0.0, attack_level: 0.608, decay: 0.225, decay_level: 0.591, sustain: 0.303, sustain_level: 0.0, release: 2.152 if sleep_vinyl_rewind(idx)
	sample :vinyl_hiss, start: 0.0, attack: 0.0, attack_level: 0.524, decay: 0.94, decay_level: 0.608, sustain: 0.443, sustain_level: 0.439, release: 0.055 if sleep_vinyl_hiss(idx)
	sample :elec_chime, start: 0.0, attack: 0.0, attack_level: 0.456, decay: 0.312, decay_level: 0.541, sustain: 0.139, sustain_level: 0.507, release: 0.383 if sleep_elec_chime(idx)
	sample :ambi_drone, start: 0.0, attack: 0.0, attack_level: 0.473, decay: 0.665, decay_level: 0.541, sustain: 0.115, sustain_level: 0.0, release: 0.196 if sleep_ambi_drone(idx)
	sample :ambi_choir, start: 0.0, attack: 0.001, attack_level: 0.473, decay: 0.225, decay_level: 0.439, sustain: 0.446, sustain_level: 0.0, release: 0.199 if sleep_ambi_choir(idx)
	sample :bass_drop_c, start: 0.0, attack: 0.0, attack_level: 0.625, decay: 0.272, decay_level: 0.507, sustain: 1.06, sustain_level: 0.524, release: 0.018 if sleep_bass_drop_c(idx)
	sample :loop_breakbeat, start: 0.0, attack: 0.0, attack_level: 0.845, decay: 0.275, decay_level: 0.845, sustain: 1.629, sustain_level: 0.963, release: 0.0 if sleep_loop_breakbeat(idx)
	sample :mehackit_phone3, start: 0.0, attack: 0.0, attack_level: 0.338, decay: 0.259, decay_level: 0.625, sustain: 0.598, sustain_level: 0.473, release: 0.254 if sleep_mehackit_phone3(idx)
	sample :drum_cymbal_hard, start: 0.0, attack: 0.0, attack_level: 0.845, decay: 0.0, decay_level: 0.828, sustain: 0.657, sustain_level: 0.0, release: 0.982 if sleep_drum_cymbal_hard(idx)
	sample :elec_filt_snare, start: 0.0, attack: 0.0, attack_level: 0.777, decay: 0.0, decay_level: 0.693, sustain: 0.779, sustain_level: 0.355, release: 0.307 if sleep_elec_filt_snare(idx)
	sleep get[:downbeat_time]
end