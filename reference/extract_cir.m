function [cir] = extract_cir(cir_str)
cir = typecast(matlab.net.base64decode(cir_str), 'uint16');
end

