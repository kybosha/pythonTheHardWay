formatter = "%r %r %r %r"

# add in the following numbers instead of the %r
print formatter % (1, 2, 3, 4)
# add in the following strings instead of the %r
print formatter % ("one", "two", "three", "four")
# add in the following boolenas instead of %r
print formatter % (True, False, False, True)
# add in the value of the formatter variable
print formatter % (formatter, formatter, formatter, formatter)
# add in the following strings
print formatter % (
		"I had this string.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
		)
