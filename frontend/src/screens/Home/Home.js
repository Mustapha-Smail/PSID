import React, { useEffect, useState } from 'react'
import './Home.css'
import axios from 'axios'
import Grid from '@mui/system/Unstable_Grid'
import { TopNav, CardGraph } from '../../components'

const Home = () => {

    const [plotData, setPlotData] = useState(null)
    const [pieData, setPieData] = useState(null)

    useEffect(() => {
        const getData = async () => {
            try {
                const { data } = await axios.get(`histogram`)
                console.log(JSON.parse(data.data));
                setPlotData(JSON.parse(data.data))
                const response = await axios.get(`data`)
                console.log(JSON.parse(response.data.data));
                setPieData(JSON.parse(response.data.data))
            } catch (err) {
                console.error(err)
            }
        }
        getData()
    }, [])

    return (
        <>
            <TopNav />
            <Grid container spacing={2}>
                <Grid xs={12} md={6}>
                    {plotData && <CardGraph plotData={plotData} />}
                </Grid>
                <Grid xs={12} md={6}>
                    {pieData && <CardGraph plotData={pieData} />}
                </Grid>
            </Grid>
        </>
    )
}

export default Home