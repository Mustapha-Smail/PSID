import React from 'react'
import './Home.css'
import Grid from '@mui/system/Unstable_Grid'
import { TopNav, CardGraph } from '../../components'

const Home = () => {

    return (
        <>
            <TopNav />
            <Grid container spacing={2}>
                <Grid xs={12} md={6}>
                    <CardGraph url={`restaurants-country`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph url={`price-diet`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph url={`popularity-diet`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph url={`distribution-restaurants`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph url={`distribution-cuisine`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph url={`distribution-satisfaction`} />
                </Grid>
            </Grid>
        </>
    )
}

export default Home