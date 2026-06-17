from lib.gratitudes import *

#Initially formats with no gratitudes
def test_initially_formats_with_no_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

# Adding one gratitude reflects in the format 
def test_adding_one_gratitude_formats_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    assert gratitudes.format() == "Be grateful for: health"

# Adding multiple gratitudes joins them together 
def test_adding_multiple_gratitudes_formats_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    gratitudes.add("family")
    gratitudes.add("coding")
    assert gratitudes.format() == "Be grateful for: health, family, coding"