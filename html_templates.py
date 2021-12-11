title_temp = """
    <div style="background-color:{};padding:10px;border-radius:10px">
    <h1 style="color:{};text-align:center;"> Hospital Management System </h1>
    </div>
    """

home_temp = """
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px;font-size:20px">
        WELCOME!
    </p>
    <p style="text-align:justify;color:black;padding:10px;font-size:20px">
        The available tables in the interface are:
        <ol style="text-align:justify;color:black;padding:10px;">
            <li font-size:20px> Doctors </l1>
            <li font-size:20px> Patients </l1>
            <li font-size:20px> Medicines </l1>
            <li font-size:20px> Insurances </l1>
        </ol>
    </p>
    <p style="text-align:justify;color:black;padding:10px;font-size:20px">
        Please choose an option from the side bar on the left.
    </p>
    </div>
    """


doctors_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">ID: {}</P>
    <p style="font-size:16px;">First Name: {}</p>
    <p style="font-size:16px;">Last Name: {}</p>
    <p style="font-size:16px;">Age: {}</p>
    <p style="font-size:16px;">Designation: {}</p>
    </div>
    """

patients_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">ID: {}</h6>
    <p style="font-size:16px;">First Name: {}</h6>
    <p style="font-size:16px;">Last Name: {}</h6>
    <p style="font-size:16px;">Gender: {}</h6>
    <p style="font-size:16px;">DOB: {}</h6>
    <p style="font-size:16px;">Phone: {}</h6>
    <p style="font-size:16px;">Address: {}</h6>
    </div>
    """

departments_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">ID: {}</h6>
    <p style="font-size:16px;">Department Name: {}</h6>
    <p style="font-size:16px;">Building Name: {}</h6>
    </div>
    """

medicines_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">ID: {}</h6>
    <p style="font-size:16px;">Medicine Name: {}</h6>
    <p style="font-size:16px;">Medicine Type: {}</h6>
    <p style="font-size:16px;">Cost: {}</h6>
    </div>
    """

insurances_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">Insurance ID: {}</h6>
    <p style="font-size:16px;">Provider Name: {}</h6>
    <p style="font-size:16px;">Expiry Date: {}</h6>
    <p style="font-size:16px;">Patient ID: {}</h6>
    </div>
    """

bills_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <p style="font-size:16px;">Bill ID: {}</h6>
    <p style="font-size:16px;">Doctor Charge: {}</h6>
    <p style="font-size:16px;">Medicine Charge: {}</h6>
    <p style="font-size:16px;">Patient ID: {}</h6>
    <p style="font-size:16px;">Insurance ID: {}</h6>
    </div>
    """
