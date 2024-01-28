import React, { useEffect, useState } from 'react'
import Grid from '@mui/system/Unstable_Grid'
import { TopNav, CardGraph, CardDetails, FlashNews, Footer } from '../../components'
import './Dashboard.css'
const Home = () => {
    const [shakingId, setShakingId] = useState(null);
    useEffect(() => {
        const hash = window.location.hash.replace('#', '');
        if (hash) {
            setShakingId(hash);
            // Optional: remove the shaking effect after some time
            setTimeout(() => setShakingId(null), 3500); // Stop shaking after 2 seconds
        }
    }, [window.location.hash]);
    return (
        <>
            <TopNav />
            <Grid container px={5} my={5}>
                <Grid lg={12}>
                    <FlashNews
                        text={"Pour la réalisation de ce dashboard, nous avons utilisé un Dataset nettoyé et sommes donc passés de 1 083 397 lignes initialement à 190 325 lignes."}
                        url={`/details`}
                    />
                </Grid>
            </Grid>
            <Grid container spacing={2} px={5}>
                <CardDetails url={`numbers`} />
                <Grid xs={12} md={6} id="restaurants-country" className={shakingId === 'restaurants-country' ? 'shake' : ''}>
                    <CardGraph details={true} url={`restaurants-country`} />
                </Grid>
                <Grid xs={12} md={6} id="price-diet" className={shakingId === 'price-diet' ? 'shake' : ''}>
                    <CardGraph details={true} url={`price-diet`} />
                </Grid>
                <Grid xs={12} md={6} id="popularity-diet" className={shakingId === 'popularity-diet' ? 'shake' : ''}>
                    <CardGraph details={true} url={`popularity-diet`} />
                </Grid>
                <Grid xs={12} md={6} id="distribution-restaurants" className={shakingId === 'distribution-restaurants' ? 'shake' : ''}>
                    <CardGraph details={true} url={`distribution-restaurants`} />
                </Grid>
                <Grid xs={12} md={6} id="note-top-eight" className={shakingId === 'note-top-eight' ? 'shake' : ''}>
                    <CardGraph details={true} url={`note-top-eight`} />
                </Grid>
                <Grid xs={12} md={6} id="distribution-satisfaction" className={shakingId === 'distribution-satisfaction' ? 'shake' : ''}>
                    <CardGraph details={true} url={`distribution-satisfaction`} />
                </Grid>
                <Grid xs={12} md={12} container>
                    <Grid xs={12} md={4} id="plot-service" className={shakingId === 'plot-service' ? 'shake' : ''}>
                        <CardGraph details={true} url={`plot-service`} />
                    </Grid>
                    <Grid xs={12} md={4} id="plot-value" className={shakingId === 'plot-value' ? 'shake' : ''}>
                        <CardGraph details={true} url={`plot-value`} />
                    </Grid>
                    <Grid xs={12} md={4} id="plot-atmosphere" className={shakingId === 'plot-atmosphere' ? 'shake' : ''}>
                        <CardGraph details={true} url={`plot-atmosphere`} />
                    </Grid>
                </Grid>
                <Grid xs={12} md={12} id="note-moyenne-restaurants" className={shakingId === 'note-moyenne-restaurants' ? 'shake' : ''}>
                    <CardGraph details={true} url={`note-moyenne-restaurants`} />
                </Grid>
            </Grid>
            <Grid container spacing={2} p={5}>
                <Grid lg={12}>
                    <Footer />
                </Grid>
            </Grid>
        </>
    )
}

export default Home