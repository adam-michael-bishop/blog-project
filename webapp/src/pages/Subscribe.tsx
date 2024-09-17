import { Container, Typography, Link } from '@mui/material'
import React from 'react'


export default function Subscribe() {
  const productLink = "https://buy.stripe.com/test_fZe4iV0ApdSa8O46oo"
  const userEmail = "abishop1993@gmail.com"

  return (
    <>
        <Container>
            <Link 
              target='_blank'
              rel='noopener'
              href={
                productLink +
                '?prefilled_email=' +
                userEmail
              }
            >
                Subscib
            </Link>
        </Container>
    </>
  )
}
