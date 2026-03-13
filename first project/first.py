import xml.etree.ElementTree as ET

data = """
<Students>
    <Level number="3">
      <Department name="CS">
        <Student id="S1">
          <name>Ahmed</name>
          <email>ahmed@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S2">
          <name>Mohamed</name>
          <email>mohamed@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S3">
          <name>Ola</name>
          <email>ola@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
      <Department name="IS">
        <Student id="S4">
          <name>Mazen</name>
          <email>mazen@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S5">
          <name>Asem</name>
          <email>asem@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S6">
          <name>Yara</name>
          <email>yara@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
      <Department name="AI">
        <Student id="S7">
          <name>Mostafa</name>
          <email>mostafa@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S8">
          <name>Nada</name>
          <email>nada@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S9">
          <name>Omar</name>
          <email>omar@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
    </Level>
  
    <Level number="4">
      <Department name="CS">
        <Student id="S10">
          <name>Heba</name>
          <email>heba@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S11">
          <name>Ali</name>
          <email>ali@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S12">
          <name>Salma</name>
          <email>salma@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
      <Department name="IS">
        <Student id="S13">
          <name>Mahmoud</name>
          <email>mahmoud@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S14">
          <name>Reem</name>
          <email>reem@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S15">
          <name>Tamer</name>
          <email>tamer@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
      <Department name="AI">
        <Student id="S16">
          <name>Hana</name>
          <email>hana@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S17">
          <name>Khaled</name>
          <email>khaled@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
        <Student id="S18">
          <name>Farah</name>
          <email>farah@gmail.com</email>
          <phone>123-456-7890</phone>
        </Student>
      </Department>
    </Level>
  </Students>
"""

tree = ET.fromstring(data)

for level in tree.findall('Level'):
    level_number = level.attrib['number']
    for dept in level.findall('Department'):
        dept_name = dept.attrib['name']
        print(f"Level {level_number} {dept_name} Students:")
        for student in dept.findall('Student'):
            print(f"Id: {student.attrib['id']}")
            print(f"Name: {student.find('name').text}")
            print(f"Email: {student.find('email').text}")
            print(f"Phone: {student.find('phone').text}\n")
        print("------------------------------------------------------------\n")