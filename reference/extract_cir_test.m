clear all;
close all;

demo_cir = "JwBqAAkARAA8AE8AJQBQAGQAPQGSBq0Nhw2iBj0VlxtzE4EEsw1MDB0I1QDZBu8FVQTKA/YBSQNlBW4FewZ2BIYCkAQBCGYFugJ4AtEBnAGQAZMC0AUtCOsG7wBABjMG0wEuAg==";
decoded = extract_cir(demo_cir);

f = figure;
plot(decoded)
