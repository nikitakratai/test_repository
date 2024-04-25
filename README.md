# test_repository
# this is my first repository in GitHub to test functions.
# 25.04.2024

# 17.02.2024 added new text to the file.

i = random(100);
if i > 50
 print('i>50');
else
  exit;
end;


# 4-th block of readme.md
# some GNSS satellite PRN generation
s = ones(1,10);
for i = 1:10
 if random(100)>50:
  s(i)=0;
 else
  s(i)=1;
 end;
end;

s2 = [];
l=1023
for i=1:l
 s2=[s2 s(10)];
 s(10)=xor(s(1:9))
 s(1)=s(10)
end;
print('s2:',s2);
end;

//what to do?
// 18.03.2024 - new string.



