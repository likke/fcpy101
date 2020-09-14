# Text source: https://en.wikipedia.org/wiki/Women_in_science
text = """
Women have made significant contributions to science from the earliest times.
Historians with an interest in gender and science have illuminated the
scientific endeavors and accomplishments of women, the barriers they have
faced, and the strategies implemented to have their work peer-reviewed and
accepted in major scientific journals and other publications. The historical,
critical and sociological study of these issues has become an academic
discipline in its own right.

The involvement of women in the field of medicine occurred in several early
civilizations, and the study of natural philosophy in ancient Greece was open
to women. Women contributed to the proto-science of alchemy in the first or
second centuries AD. During the Middle Ages, convents were an important place
of education for women, and some of these communities provided opportunities
for women to contribute to scholarly research. While the eleventh century saw
the emergence of the first universities, women were, for the most part,
excluded from university education. Outside academia, botany was the science
that benefitted most from contributions of women in early modern times. The
attitude toward educating women in medical fields appears to have been more
liberal in Italy than in other places. The first known woman to earn a
university chair in a scientific field of studies was eighteenth-century
Italian scientist Laura Bassi.
"""

# func to separate string from separator
def convert(string, separator): 
    li = list(string.split(separator))
    return li

# Any characters you want to ignore when comparing
import re; 

woman_counter = 0
word_counter = 0

clean_text = re.sub(r'[^\w]+', ' ', text.rstrip('\n'));
clean_text_list = clean_text.split(" ")
print(clean_text_list)

dict_words = {}

for i in clean_text_list:
    if i not in dict_words:
        dict_words[i] = 1
    else:
         dict_words[i] += 1

    if str(i).lower() == 'woman':
      woman_counter += 1
    if str(i).lower() == 'women':
      woman_counter += 1
    if i != "":
      word_counter += 1

sort_dict_words = {k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1])}

print(f"Word count: {word_counter} \n Number of women: {woman_counter}")
print(sort_dict_words)