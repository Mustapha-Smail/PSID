import React from 'react'
import Grid from '@mui/system/Unstable_Grid'
import { TopNav, CardGraph, CardDetails } from '../../components'

const Home = () => {

    return (
        <>
            <TopNav />
            <Grid container spacing={2} p={5}>
                <CardDetails url={`numbers`} />
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`restaurants-country`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`price-diet`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`popularity-diet`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`distribution-restaurants`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`note-top-eight`} />
                </Grid>
                <Grid xs={12} md={6}>
                    <CardGraph details={true} url={`distribution-satisfaction`} />
                </Grid>
                <Grid xs={12} md={12} container>
                    <Grid xs={12} md={4}>
                        <CardGraph details={true} url={`plot-service`} />
                    </Grid>
                    <Grid xs={12} md={4}>
                        <CardGraph details={true} url={`plot-value`} />
                    </Grid>
                    <Grid xs={12} md={4}>
                        <CardGraph details={true} url={`plot-atmosphere`} />
                    </Grid>
                </Grid>
                <Grid xs={12} md={12}>
                    <CardGraph details={true} url={`note-moyenne-restaurants`} />
                </Grid>
            </Grid>
        </>
    )
}

export default Home