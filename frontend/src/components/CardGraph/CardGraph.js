import { CardContent, Divider, Typography, Card } from '@mui/material'
import { Stack } from '@mui/system'
import React from 'react'
import Plot from 'react-plotly.js'

const CardGraph = ({ plotData }) => {
    return (
        <Card sx={{ borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)' }}>
            <CardContent>
                <Stack spacing={1}>
                    <Stack spacing={1}>
                        <Typography
                            color="text.secondary"
                            variant="overline"
                        >
                            {/* {plotData && plotData.layout.title.text} */}
                        </Typography>
                        <Divider />
                        <Typography>
                            <Plot data={plotData.data} layout={{ width: '100%', height: '100%', title: plotData.layout.title }} />
                        </Typography>
                    </Stack>

                </Stack>
            </CardContent>
        </Card>
    )
}

export default CardGraph