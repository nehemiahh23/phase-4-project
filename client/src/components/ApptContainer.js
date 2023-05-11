import React from 'react'
import ApptCard from './ApptCard'
import { useEffect, useState } from 'react'

function ApptContainer({owner, doctor, pet_appointment, setPetAppointment}) {

    const [arr, setArr] = useState([])
    const [showDiv, setDiv] = useState(false)
    

    // pass doctor prop from App > Desk
    useEffect(() => {
        if(owner) {
            fetch(`/owner-appointments/${owner.id}`)
            .then(response=> {
                if(response.ok) {
                    response.json()
                    .then(data => setArr(data))
                }
                
            })
           
        }

        else if(doctor) {
            fetch(`doctor-appointments/${doctor.id}`)
            .then(response=> {
                if(response.ok) {
                    response.json()
                    .then(data=> setArr(data))
                }
            })
            

        }
    },[])
        

        
        

    const cardArr = arr.map(appt => <ApptCard key={appt.id} owner={owner} setPetAppointment={setPetAppointment} setDiv={setDiv} showDiv={showDiv} doctor={doctor} appt={appt}/>)
    console.log(cardArr)

    return (
        <div>
            <h3>Appointments</h3>
            {cardArr.length ? <ol> {cardArr} </ol>: "No appointments"}
        

        </div>
    )
}

export default ApptContainer