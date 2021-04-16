# json file
{ "School" : "St Joseph High School",
  "Class":"9",
  "City":"Bangalore",
  "Students":[  { "ID":"1",
                 "Name":"Sohan",
                 "Age":"16"
                },
                { "ID":"2",
                 "Name":"Abhay",
                 "Age":"15"
                },
                { "ID":"3",
                 "Name":"John",
                 "Age":"16"
                },
			    { "ID":"4",
                 "Name":"Nancy",
                 "Age":"15"
                }
             ]
}

#json path values
#1-$.School
#optput
[
  "St Joseph High School"
]
#2-$.Students
# output
[
  [
    {
      "ID": "1",
      "Name": "Sohan",
      "Age": "16"
    },
    {
      "ID": "2",
      "Name": "Abhay",
      "Age": "15"
    },
    {
      "ID": "3",
      "Name": "John",
      "Age": "16"
    },
    {
      "ID": "4",
      "Name": "Nancy",
      "Age": "15"
    }
  ]
]

#3-$.Students[0]
#output
[
  {
    "ID": "1",
    "Name": "Sohan",
    "Age": "16"
  }
]

#4-$.Students[0].Name
#output
[
  "Sohan"
]

#5-$.Students[0,1,2].Name
#output
[
  "Sohan",
  "Abhay",
  "John"
]

#6-$.Students[0:3].Name
#output
[
  "Sohan",
  "Abhay",
  "John"
]
#7-$.Students[*].Name
#output
[
  "Sohan",
  "Abhay",
  "John",
  "Nancy"
]

#8-$.Students[0:-1].Name
#output
[
  "Sohan",
  "Abhay",
  "John"
]
