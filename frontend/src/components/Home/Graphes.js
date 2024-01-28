import { Grid } from '@mui/material'
import React from 'react'
import CardGraph from '../CardGraph/CardGraph'
import Feature from './Feature'

const Graphes = () => {
    return (
        <Grid
            container
            spacing={2}
            p={5}
        >
            <Grid
                container
                spacing={2}
                p={5}
            >
                <Grid
                    xs={12}
                    md={6}
                >
                    <Feature
                        title="L'Europe, un buffet de cultures"
                        text="En Europe, la gastronomie est un regroupement d'origine, de saveurs et d'expériences, reflétant la richesse culturelle de chaque nation. Au cœur de ce paysage culinaire, l'Italie possède le plus grand nombre de restaurants, ce qui peut montrer une tradition gastronomique enracinée. Cependant, ce n'est pas seulement une question de quantité ; on peut voir que la diversité alimentaire y est également manifeste, avec une multitude d'options répondant aux besoins des végétariens, des végans et de ceux qui suivent un régime sans gluten."
                    />
                </Grid>
                <Grid
                    xs={12}
                    md={6}
                >
                    <CardGraph url={`restaurants-country`} />
                </Grid>
            </Grid>
            <Grid
                container
                spacing={3}
                p={5}
            >
                <Grid
                    xs={12}
                    md={3}
                    paddingRight={1}
                >
                    <Feature
                        title="L'adaptation comme clé du succès"
                        text="L'adaptabilité est devenue un point important des restaurateurs européens. Depuis quelques années les modes de vie changent et la manifestation des régimes spéciaux augmente, les restaurants à travers le continent ont donc dû s'adapter. "
                    />
                </Grid>
                <Grid
                    xs={12}
                    // mx={1}
                    md={6}
                >
                    <CardGraph url={`popularity-diet`} />
                </Grid>
                <Grid
                    xs={12}
                    md={3}
                    paddingLeft={2}
                >
                    <Feature
                        // title='Deuxième Graphe'
                        text="Cela ne se reflète pas nécessairement dans une augmentation des avis ou des évaluations, mais c'est un sujet que les clients considèrent maintenant dans leur notation."
                    />
                </Grid>
            </Grid>
            <Grid
                container
                spacing={3}
                p={5}
            >

                <Grid
                    xs={12}
                    mx={2}
                    md={6}
                >
                    <CardGraph url={`distribution-satisfaction`} />
                </Grid>
                <Grid
                    xs={12}
                    md={4}
                >
                    <Feature
                        title='Le meilleur rapport qualité-prix'
                        text="Si nous prenons l'exemple des cuisines les plus fréquentes en Europe, on découvre que le rapport qualité-prix ne discrimine pas selon l'origine de la cuisine. Des cuisines aussi variées que la cuisine marocaine, indienne, et la japonaise tiennent tête à la prestigieuse gastronomie française, avec la cuisine indienne se distinguant particulièrement pour son rapport qualité-prix. "
                    />
                </Grid>
            </Grid>
        </Grid>
    )
}

export default Graphes