import subprocess

output = None
print("Running Build:")
try:
    output = subprocess.check_output(['sh', './build.sh'], stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    output = e.output

print(output)

# build_output_bytes = subprocess.check_output(
# build_output = build_output_bytes.decode("utf-8")
# print(build_output)