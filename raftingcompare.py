
# file to compare the descriptions of three different
# white water rafting trips. descriptions taken from website
# and put into text files.



with open('standard.txt', 'r') as file1:
    with open('deluxe.txt', 'r') as file2:
        different_std_dlx = set(file2).difference(file1)
# for sets, set difference aka setA-setB is the equivalent
# of saying what is in setA that isn't also in setB?
# so for the difference of the deluxe vs standard we have to ask
# for set(file2).difference(file1)

with open('deluxe.txt', 'r') as file3:
    with open('ultimate.txt', 'r') as file4:
        different_ult_dlx = set(file4).difference(file3)

different_std_dlx.discard('\n')# get rid of new lines
different_ult_dlx.discard('\n')

with open('deluxe_over_standard.txt', 'w') as file_out:
    for line in different_std_dlx:
        file_out.write(line)

with open('ultimate_over_deluxe.txt', 'w') as file_out:
    for line in different_ult_dlx:
        file_out.write(line)
