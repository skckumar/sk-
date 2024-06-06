import streamlit as st

def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.postimg.cc/nhX3KfVw/synthwave-car-ai-162023.png");
            background-size: cover;
  <font color="white"></font>
        """,
        unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    .reportview-container {
        background: rgba(0, 0, 0, 0.5);
        background-size: cover;
    }
    .sidebar .sidebar-content {
        background: rgba(0, 0, 0, 0.5);
    }
    pre {
        background: rgba(2, 2, 2, 0.5) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Call the function to add custom CSS
add_custom_css()
st.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Html with Sk</title>
</head>
<body background="synthwave-car-ai-162023.png">
 

""")
st.sidebar.title("Learn html with Sk")
st.sidebar.image("we.png")
st.sidebar.link_button("Youtube","https://youtube.com/shorts/t2s5MqeU9jI?si=bebqULeE31Bn7Qq2")
st.sidebar.link_button("instagram","https://www.instagram.com/shivam_python_700?igsh=Z3lpNjNkczB2aHp5")
st.title("Learn Html with Sk")
st.text("start html code")


st.code("""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

</body>
</html>
""")
st.text("Paragraph tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Paragraph Tag</title>
</head>

<body>

 <p>This is the First Paragraph starting</p>
 <p>This is the Second Paragraph starting</p>
 <p>This is the Fourth Paragraph starting</p>
 <p>This is the Fifth Paragraph starting</p>

</body>

</html>
""")
st.text("Heading")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Heading in HTML</title>
</head>

<body>

 <h1>Heading1</h1>
 <h2>Heading2</h2>
 <h3>Heading3</h3>
 <h4>Heading4</h4>
 <h5>Heading5</h5>
 <h6>Heading6</h6>

</body>

</html>
""")
st.text("Horizontal Line")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Horizontal Line</title>
</head>

<body>

 First Line
 <hr> Second Line
 <hr> Third Line
 <hr>

</body>

</html>
""")
st.text("Horizontal Line color")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Horizontal Line color</title>
</head>

<body>

 First Line
 <hr color="red"> Second Line
 <hr color="green"> Third Line
 <hr color="blue">

</body>

</html>
""")
st.text("Horizontal Line size")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Horizontal Line size</title>
</head>

<body>

 First Line
 <hr size="10px" color="red"> Second Line
 <hr size="30px" color="green"> Third Line
 <hr color="blue">

</body>

</html>
""")
st.text("Horizontal Line width")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Horizontal Line width</title>
</head>

<body>

 First Line
 <hr width="50%" size="10px" color="red"> Second Line
 <hr width="80%" color="green"> Third Line
 <hr color="blue">

</body>

</html>
""")
st.text("Div can be used to group elements")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>div tag</title>
</head>

<body>

 <!--Div can be used to group elements-->
 <div>
  This is the First Div
  <input type="text">
  <input type="text">
  <input type="text">
 </div>

 <div>
  This is the Second Div
  <input type="text">
  <button>Sample Button</button>
 </div>

</body>

</html>
""")
st.html(""" <div>
  This is the First Div
  <br>
  <input type="text">
  <input type="text">
  <input type="text">
 </div>
<br>
 <div>
  This is the Second Div
  <input type="text">
  <button>Sample Button</button>
 </div>

""")
st.text("Mark tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>mark tag</title>
</head>

<body>

 Normal Text
 <br> mark <mark>This</mark> Text

</body>

</html>
""")
st.text("Delete tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Delete</title>
</head>

<body>

 This is the <del>Deleted Text</del>

</body>

</html>
""")
st.text("Insert tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Insert</title>
</head>

<body>

 This is the <ins>Inserted Text</ins>

</body>

</html>
""")
st.text("subscripted Text")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>subscripted Text</title>
</head>

<body>

 This is the <sub>subscripted</sub> Text

</body>

</html>
""")
st.html("""
<body>

 This is the <sub>subscripted</sub> Text

</body>
""")
st.text("Superscriptet text")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>superscripted Text</title>
</head>

<body>

 This is the <sup>superscripted</sup> Text

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>superscripted Text</title>
</head>

<body>

 This is the <sup>superscripted</sup> Text

</body>

</html>
""")
st.text("strong tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Strong tag</title>
</head>

<body>

 This is the <strong>Strong Text</strong>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Strong tag</title>
</head>

<body>

 This is the <strong>Strong Text</strong>

</body>

</html>
""")
st.text("BR Tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>BR Tag</title>
</head>

<body>

 <!--Without BR Tag-->
 Line 1
 Line 2
 Line 3
 Line 4
 Line 5

 <!--With using BR Tag-->
 <br> Line 1
 <br> Line 2
 <br> Line 3
 <br> Line 4
 <br> Line 5

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>BR Tag</title>
</head>

<body>

 <!--Without BR Tag-->
 Line 1
 Line 2
 Line 3
 Line 4
 Line 5

 <!--With using BR Tag-->
 <br> Line 1
 <br> Line 2
 <br> Line 3
 <br> Line 4
 <br> Line 5

</body>

</html>
""")
st.text("s tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>s tag</title>
</head>

<body>

 <s>This is the</s> HTML Code Play

</body>

</html>
""")
st.text("Quotation")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Quotation</title>
</head>

<body>

 He said <q>This is too much.</q>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Quotation</title>
</head>

<body>

 He said <q>This is too much.</q>

</body>

</html>
""")
st.text("Address")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Address</title>
</head>

<body>

 My Address is.
 <Address>
    Ramesh,<br>
	Kozicode,<br>
	Chennai,<br>
	Pin-629167,<br>
	K.K.Dist.
  </Address>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Address</title>
</head>

<body>

 My Address is.
 <Address>
    Ramesh,<br>
	Kozicode,<br>
	Chennai,<br>
	Pin-629167,<br>
	K.K.Dist.
  </Address>

</body>

</html>
""")
st.text("bdo tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>bdo</title>
</head>

<body>

 This is normal text
 <br>
 <bdo dir="rtl">Right to Left Direction</bdo>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>bdo</title>
</head>

<body>

 This is normal text
 <br>
 <bdo dir="rtl">Right to Left Direction</bdo>

</body>

</html>
""")
st.text("kdb")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>kdb</title>
</head>

<body>

 kbd define keyboard input
 <br>
 <kbd>This text style different</kbd>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>kdb</title>
</head>

<body>

 kbd define keyboard input
 <br>
 <kbd>This text style different</kbd>

</body>

</html>
""")
st.text("code")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>code</title>
</head>

<body>

 Usually programming code are written inside the code tag.
 <br>
 <code>
	var a=10;<br>
	var b=30;<br>
	var c=0;<br>	
	c=a+b;<br>
	alert(c);<br>
  </code>

</body>

</html>
""")
st.text("var Tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>var Tag</title>
</head>

<body>

 var tag is defined mathamatical variable.
 <br>
 <var>(a+b)<sup>2</sup></var>=<var>a</var><sup>2</sup>+<var>b</var><sup>2</sup>+<var>2ab</var>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>var Tag</title>
</head>

<body>

 var tag is defined mathamatical variable.
 <br>
 <var>(a+b)<sup>2</sup></var>=<var>a</var><sup>2</sup>+<var>b</var><sup>2</sup>+<var>2ab</var>

</body>

</html>
""")
st.text("Blockquote Tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Blockquote Tag</title>
</head>

<body>

 The following paragraph is said.
 <blockquote>
  This paragraph is highlighted separately, because this lines are inside the blockquote tag. So we know this will display in a block.
 </blockquote>

</body>

</html>
""")
st.text("Contenteditable")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Contenteditable</title>
</head>

<body>

 For P Tag
 <p contenteditable="true">This is the paragraph(p) tag [Click Here]</p>
 <br> Div Tag
 <br>
 <div contenteditable="true">This is the Div element [Click Here]</div>
 <br> Span Tag
 <br>
 <span contenteditable="true">This is the span element [Click Here]</span>

</body>

</html>
""")
st.text("Center tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Center tag</title>
</head>

<body>

 <center>This is the text display in center</center>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Center tag</title>
</head>

<body>

 <center>This is the text display in center</center>

</body>

</html>
""")
st.text("TextBox")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>TextBox</title>
</head>

<body>

 <input type="text" value="12345" size="5" maxlength="3">

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>TextBox</title>
</head>

<body>

 <input type="text" value="12345" size="5" maxlength="3">

</body>

</html>
""")

st.text("password")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>password</title>
</head>

<body>

 Username:
 <input type="text">
 <br> Password :
 <input type="password">

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>password</title>
</head>

<body>

 Username:
 <input type="text">
 <br> Password :
 <input type="password">

</body>

</html>
""")

st.text("Text Area")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Text Area</title>
</head>

<body>

 <textarea cols="5" rows="5"></textarea>

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Text Area</title>
</head>

<body>

 <textarea cols="5" rows="5"></textarea>

</body>

</html>
""")

st.text("Button")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Button</title>
</head>

<body>

 <input type="button" value="Click Me">

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Button</title>
</head>

<body>

 <input type="button" value="Click Me">

</body>

</html>
""")

st.text("Auto Focus on button")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Auto Focus on button</title>
</head>

<body>

 <button>Test Button</button>
 <button autofocus="true">Test Button Focused</button>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Auto Focus on button</title>
</head>

<body>

 <button>Test Button</button>
 <button autofocus="true">Test Button Focused</button>

</body>

</html>
""")

st.text("Disabled Button")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Disabled Button</title>
</head>

<body>

 <button>Normal Button</button>
 <button disabled="true">Disabled Button</button>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Disabled Button</title>
</head>

<body>

 <button>Normal Button</button>
 <button disabled="true">Disabled Button</button>

</body>

</html>
""")
st.text("Radio Button")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Radio Button</title>
</head>

<body>

 <!--
  You should click the checkbox, if you click on the 'Male' or 'Female' text will not check the radio button
  -->
 <input type="radio" name="gndr">Male

 <input type="radio" name="gndr">FeMale

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Radio Button</title>
</head>

<body>

 <!--
  You should click the checkbox, if you click on the 'Male' or 'Female' text will not check the radio button
  -->
 <input type="radio" name="gndr">Male

 <input type="radio" name="gndr">FeMale

</body>

</html>
""")

st.text("Check Box")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Check Box</title>
</head>

<body>

 <!--you should click the checkbox-->
 <input type="checkbox" name="gndr">Male

 <input type="checkbox" name="gndr">FeMale

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Check Box</title>
</head>

<body>

 <!--you should click the checkbox-->
 <input type="checkbox" name="gndr">Male

 <input type="checkbox" name="gndr">FeMale

</body>

</html>
""")
st.text("Links in HTML")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Links in HTML</title>
</head>

<body>

 <a href="http://www.allinworld99.blogspot.com">Open Allinworld99</a>
 <br>
 <a href="http://www.allinworld99.blogspot.com" target="_blank">Open Allinworld99 in new tab</a>

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Links in HTML</title>
</head>

<body>

 <a href="http://www.allinworld99.blogspot.com">Open Allinworld99</a>
 <br>
 <a href="http://www.allinworld99.blogspot.com" target="_blank">Open Allinworld99 in new tab</a>

</body>

</html>
""")
st.text("Images")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Images</title>
</head>

<body>

 <img src="we.jpg" width="100" height="100">
 <img src="we.jpg" alt="Sample Image" width="100" height="100">

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Images</title>
</head>

<body>

 <img src="we.png" width="100" height="100">
 <img src="we.png" alt="Sample Image" width="100" height="100">

</body>

</html>
""")
st.text("Fieldset")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Fieldset</title>
</head>

<body>

 <fieldset>
  <legend>Fieldset 1</legend>
  <p>Write your name (simple textbox): <input type="text" /></p>

  <fieldset>
   <legend>Fieldset 2</legend>
   This is the test fieldset
  </fieldset>

  <p>Write a comment:<br />
   <textarea></textarea></p>

 </fieldset>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Fieldset</title>
</head>

<body>

 <fieldset>
  <legend>Fieldset 1</legend>
  <p>Write your name (simple textbox): <input type="text" /></p>

  <fieldset>
   <legend>Fieldset 2</legend>
   This is the test fieldset
  </fieldset>

  <p>Write a comment:<br />
   <textarea></textarea></p>

 </fieldset>

</body>

</html>
""")
st.text("Inline Styl")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Inline Style</title>
</head>

<body>

 <div style="background:red;color:white;">
  Inline style Example
 </div>

</body>

</html>""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Inline Style</title>
</head>

<body>

 <div style="background:red;color:white;">
  Inline style Example
 </div>

</body>

</html>""")
st.text("Dropdown List")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Dropdown List</title>
</head>

<body>

 <select>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    <option value="4">Four</option>
    <option value="5">Five</option>
  </select>

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Dropdown List</title>
</head>

<body>

 <select>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    <option value="4">Four</option>
    <option value="5">Five</option>
  </select>

</body>

</html>
""")
st.text("Multiple Item")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Multiple Items</title>
</head>

<body>

 <select multiple>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    <option value="4">Four</option>
    <option value="5">Five</option>
  </select>

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Multiple Items</title>
</head>

<body>

 <select multiple>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    <option value="4">Four</option>
    <option value="5">Five</option>
  </select>

</body>

</html>
""")

st.text("optgroup")

st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>optgroup</title>
</head>

<body>

 <select>

    <optgroup label="Group 1">
      <option>Option 1.1</option>
    </optgroup> 

    <optgroup label="Group 2">
      <option>Option 2.1</option>
      <option>Option 2.2</option>
    </optgroup>

    <optgroup label="Group 3" disabled>
      <option>Option 3.1</option>
      <option>Option 3.2</option>
      <option>Option 3.3</option>
    </optgroup>

</select>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>optgroup</title>
</head>

<body>

 <select>

    <optgroup label="Group 1">
      <option>Option 1.1</option>
    </optgroup> 

    <optgroup label="Group 2">
      <option>Option 2.1</option>
      <option>Option 2.2</option>
    </optgroup>

    <optgroup label="Group 3" disabled>
      <option>Option 3.1</option>
      <option>Option 3.2</option>
      <option>Option 3.3</option>
    </optgroup>

</select>

</body>

</html>
""")

st.text("HTML Tabl")

st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>HTML Table</title>
</head>

<body>

 <table border="5">
  <tr>
   <th>Name</th>
   <th>Internal 1</th>
   <th>Internal 2</th>
   <th>Internal 3</th>
   <th>Internal 4</th>
  </tr>

  <tr>
   <td>Rajesh</td>
   <td>56</td>
   <td>69</td>
   <td>85</td>
   <td>91</td>
  </tr>

  <tr>
   <td>Franklin</td>
   <td>88</td>
   <td>87</td>
   <td>95</td>
   <td>92</td>
  </tr>

  <tr>
   <td>Merbin</td>
   <td>81</td>
   <td>88</td>
   <td>87</td>
   <td>89</td>
  </tr>

  <tr>
   <td>Deepa</td>
   <td>88</td>
   <td>59</td>
   <td>62</td>
   <td>67</td>
  </tr>

  <tr>
   <td>Khan</td>
   <td>57</td>
   <td>45</td>
   <td>44</td>
   <td>51</td>
  </tr>

  <tr>
   <td>Ramesh</td>
   <td>40</td>
   <td>38</td>
   <td>49</td>
   <td>56</td>
  </tr>
 </table>

</body>

</html>
""")

st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>HTML Table</title>
</head>

<body>

 <table border="1">
  <tr>
   <th>Name</th>
   <th>Internal 1</th>
   <th>Internal 2</th>
   <th>Internal 3</th>
   <th>Internal 4</th>
  </tr>

  <tr>
   <td>Rajesh</td>
   <td>56</td>
   <td>69</td>
   <td>85</td>
   <td>91</td>
  </tr>

  <tr>
   <td>Franklin</td>
   <td>88</td>
   <td>87</td>
   <td>95</td>
   <td>92</td>
  </tr>

  <tr>
   <td>Merbin</td>
   <td>81</td>
   <td>88</td>
   <td>87</td>
   <td>89</td>
  </tr>

  <tr>
   <td>Deepa</td>
   <td>88</td>
   <td>59</td>
   <td>62</td>
   <td>67</td>
  </tr>

  <tr>
   <td>Khan</td>
   <td>57</td>
   <td>45</td>
   <td>44</td>
   <td>51</td>
  </tr>

  <tr>
   <td>Ramesh</td>
   <td>40</td>
   <td>38</td>
   <td>49</td>
   <td>56</td>
  </tr>
 </table>

</body>

</html>
""")

st.text("progress bar")

st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>progress bar</title>
</head>

<body>

 <progress></progress>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>progress bar</title>
</head>

<body>

 <progress></progress>

</body>

</html>
""")

st.text("progress bar")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>progress bar</title>
</head>

<body>

 <progress value="70" max="100">70 %</progress>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>progress bar</title>
</head>

<body>

 <progress value="70" max="100">70 %</progress>

</body>

</html>
""")
st.text("Meter Tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Meter Tag</title>
</head>

<body>

 <p>Mark is : <meter>B</meter> on the exam.</p>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Meter Tag</title>
</head>

<body>

 <p>Mark is : <meter>B</meter> on the exam.</p>

</body>

</html>
""")
st.text("Meter high")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Meter high</title>
</head>

<body>

 <p>Mark is : <meter low="69" high="80" max="100" value="84">B</meter> on the exam.</p>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Meter high</title>
</head>

<body>

 <p>Mark is : <meter low="69" high="80" max="100" value="84">B</meter> on the exam.</p>

</body>

</html>
""")

st.text("Map tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Map tag</title>
</head>

<body>

 <p>The image was split into 3 part and every part will take you to different link</p>

 <img src="uk.jpg" alt="Natural Image" usemap="#natural">

 <map name="natural">
  <area shape="rect" coords="0,0,725,100" alt="First Area" href="map1.html">
  <area shape="rect" coords="0,100,725,200" alt="Second Area" href="map2.html">
  <area shape="rect" coords="0,200,725,300" alt="Third Area" href="map3.html">
</map>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Map tag</title>
</head>

<body>

 <p>The image was split into 3 part and every part will take you to different link</p>

 <img src="uk.jpg" alt="uk image" usemap="#uk">

 <map name="uk">
  <area shape="rect" coords="0,0,725,100" alt="First Area" href="map1.html">
  <area shape="rect" coords="0,100,725,200" alt="Second Area" href="map2.html">
  <area shape="rect" coords="0,200,725,300" alt="Third Area" href="map3.html">
</map>

</body>

</html>
""")
st.text("Colour Picker")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Colour Picker</title>
</head>

<body>

 <!--Default Color is Black-->
 <input type="color" />

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Colour Picker</title>
</head>

<body>

 <!--Default Color is Black-->
 <input type="color" />

</body>

</html>
""")

st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Set default Colour</title>
</head>

<body>

 <!--Default Color is Black-->
 <input type="color" value="#00FF00" />

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Set default Colour</title>
</head>

<body>

 <!--Default Color is Black-->
 <input type="color" value="#00FF00" />

</body>

</html>
""")
st.text("Date Picker")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Date Picker</title>
</head>

<body>

 <input type="date" />

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Date Picker</title>
</head>

<body>

 <input type="date" />

</body>

</html>
""")
st.text("Time Picker")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Time Picker</title>
</head>

<body>
 <!--24 Hours format-->
 <input type="time" />
</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Time Picker</title>
</head>

<body>
 <!--24 Hours format-->
 <input type="time" />
</body>

</html>
""")

st.text("Search")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Search</title>
</head>

<body>

 <input type="search" />

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Search</title>
</head>

<body>

 <input type="search" />

</body>

</html>
""")
st.text("email")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>email</title>
</head>

<body>

 <form onsubmit="return false;">
  Email: <input type="email" title="Enter valid E-mail">
  <input type="submit">
 </form>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>email</title>
</head>

<body>

 <form onsubmit="return false;">
  Email: <input type="email" title="Enter valid E-mail">
  <input type="submit">
 </form>

</body>

</html>
""")
st.text("URL")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>URL</title>
</head>

<body>

 <form onsubmit="return false;">
  Enter URL :
  <input type="url">
  <input type="submit" value="URL Validate">
 </form>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>URL</title>
</head>

<body>

 <form onsubmit="return false;">
  Enter URL :
  <input type="url">
  <input type="submit" value="URL Validate">
 </form>

</body>

</html>
""")
st.text("Number")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Number</title>
</head>

<body>
 <!--Only allow Number-->
 <input type="number">

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Number</title>
</head>

<body>
 <!--Only allow Number-->
 <input type="number">

</body>

</html>
""")
st.text("Date time Local")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Date time Local</title>
</head>

<body>

 <input type="datetime-local">

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Date time Local</title>
</head>

<body>

 <input type="datetime-local">

</body>

</html>
""")

st.text("output")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output</title>
</head>

<body>

 <input type="range" value="3" oninput="OP1.value=this.value;">

 <output id="OP1">3</output>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output</title>
</head>

<body>

 <input type="range" value="3" oninput="OP1.value=this.value;">

 <output id="OP1">3</output>

</body>

</html>
""")
st.text("output")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output</title>
</head>

<body>

 <form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
  <input type="range" name="b" value="50" /> +
  <input type="number" name="a" value="10" /> =

  <output name="result"></output>

 </form>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output</title>
</head>

<body>

 <form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
  <input type="range" name="b" value="50" /> +
  <input type="number" name="a" value="10" /> =

  <output name="result"></output>

 </form>

</body>

</html>
""")
st.text("output Tag Sample")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output Tag Sample</title>
</head>

<body>

 Sample 1 (Simple eg)
 <br> Type Here : <input type="text" onkeyup="OP.value=this.value">
 <output id="OP"></output>

 <br><br> Sample 2 (Range eg)
 <br>
 <input type="range" value="3" oninput="OP1.value=this.value;"><output id="OP1">3</output>

 <br><br> Sample 3 (Calculation eg)
 <br>

 <form oninput="Ans.value=parseInt(Fid.value)+parseInt(Sid.value)">
  <br>
  <input type="number" id="Fid"> + <input type="number" id="Sid"> =
  <output name="Ans"></output>
 </form>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>output Tag Sample</title>
</head>

<body>

 Sample 1 (Simple eg)
 <br> Type Here : <input type="text" onkeyup="OP.value=this.value">
 <output id="OP"></output>

 <br><br> Sample 2 (Range eg)
 <br>
 <input type="range" value="3" oninput="OP1.value=this.value;"><output id="OP1">3</output>

 <br><br> Sample 3 (Calculation eg)
 <br>

 <form oninput="Ans.value=parseInt(Fid.value)+parseInt(Sid.value)">
  <br>
  <input type="number" id="Fid"> + <input type="number" id="Sid"> =
  <output name="Ans"></output>
 </form>

</body>

</html>
""")
st.text("iframe example")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>iframe example</title>
</head>

<body>

 <!--Need Internet Connection-->
 <iframe src="http://google.com"></iframe>

</body>

</html>
""")
st.text("iframe example")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>iframe example</title>
</head>

<body>

 <!--Need Internet Connection-->
 <iframe width="150px" height="150px" src="http://allinworld99.blogspot.com"></iframe>

</body>

</html>
""")
st.text("youtube Integration")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>youtube Integration</title>
</head>

<body>

 <!--Need Internet Connection-->
 <iframe width="420" height="315" src="https://www.youtube.com/embed/WsB0DNhWEq8"></iframe>

</body>

</html>
""")
st.text("video tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>

 <video width="480" src="video.mp4">
  </video>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>

 <video width="480" src="https://youtube.com/shorts/aite58DAku0?si=qmnzgiNP4R2W-mQ1.mp4">
  </video>

</body>

</html>
""")

st.text("simple marquee text")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Simple Marquee</title>
</head>

<body>

 <marquee>
  <h1>Test Marquee</h1>
 </marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Simple Marquee</title>
</head>

<body>

 <marquee>
  <h1>Test Marquee</h1>
 </marquee>

</body>

</html>
""")
st.text("Marquee Right")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Right</title>
</head>

<body>

 <marquee direction="right">
  <h1>Right Direction</h1>
 </marquee>

</body>

</html>
""")

st.text("Direction up")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Direction up</title>
</head>

<body>

 <marquee direction="up">
  <h1>Direction Up</h1>
 </marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Behavior</title>
</head>

<body>

 <!--Rotate only once-->
 <marquee behavior="alternate">
  <h1>Test Marquee</h1>
 </marquee>

</body>

</html>
""")
st.text("Marquee Behavior")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Behavior</title>
</head>

<body>

 <!--Rotate only once-->
 <marquee behavior="alternate">
  <h1>Test Marquee</h1>
 </marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Behavior</title>
</head>

<body>

 <!--Rotate only once-->
 <marquee behavior="alternate">
  <h1>Test Marquee</h1>
 </marquee>

</body>

</html>
""")
st.text("Marquee Alternative")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Alternative</title>
</head>

<body>

 <!--Will not go away from the screen-->
 <marquee behavior="alternate">
  <h1>Moving Alternative</h1>
 </marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee Alternative</title>
</head>

<body>

 <!--Will not go away from the screen-->
 <marquee behavior="alternate">
  <h1>Moving Alternative</h1>
 </marquee>

</body>

</html>
""")
st.text("Marquee scrollamount")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee scrollamount</title>
</head>

<body>

 <marquee scrollamount="20" behavior="alternate">
  <h1>Moving scrollamount</h1>
 </marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Marquee scrollamount</title>
</head>

<body>

 <marquee scrollamount="20" behavior="alternate">
  <h1>Moving scrollamount</h1>
 </marquee>

</body>

</html>
""")
st.text("First HTML")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>First HTML</title>
</head>

<body>

 <marquee onmouseover="this.stop();" onmouseout="this.start();">Mouse over and release</marquee>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>First HTML</title>
</head>

<body>

 <marquee onmouseover="this.stop();" onmouseout="this.start();">Mouse over and release</marquee>

</body>

</html>
""")
st.text("style tag")
st.code("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">

 <style>
  .clsname {
   color: green;
   font-size: 40px;
  }
 </style>

</head>

<body>

 <div class="clsname">
  Android Code Play
 </div>

</body>
""")
st.html("""
<!DOCTYPE html>
<html>

<head>
 <meta name="viewport" content="width=device-width, initial-scale=1">

 <style>
  .clsname {
   color: green;
   font-size: 40px;
  }
 </style>

</head>

<body>

 <div class="clsname">
  Android Code Play
 </div>

</body>
""")
st.text("canvas")
st.code("""
<!DOCTYPE html>
<html>

<body>

 <canvas style="border:1px solid" id="rect" width="300" height="300"></canvas>

 <script>
  var canvas = document.getElementById('rect');
  var ctx = canvas.getContext('2d');
  ctx.fillStyle = 'red';
  ctx.fillRect(50, 20, 50, 50);
 </script>

</body>

</html>
""")
st.html("""
<!DOCTYPE html>
<html>

<body>

 <canvas style="border:1px solid" id="rect" width="300" height="300"></canvas>

 <script>
  var canvas = document.getElementById('rect');
  var ctx = canvas.getContext('2d');
  ctx.fillStyle = 'red';
  ctx.fillRect(50, 20, 50, 50);
 </script>

</body>

</html>
""")
