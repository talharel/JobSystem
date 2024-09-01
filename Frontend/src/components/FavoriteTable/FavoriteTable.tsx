import { useEffect, useState } from 'react';
import './FavoriteTable.css';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import Button from '@mui/material/Button';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import companyService from '../../services/companyService';
import { TypeCompany } from '../../utils/types';
import { Typography } from '@mui/material';
import TextField from '@mui/material/TextField';
import BasicModal from '../Modal/Modal';

export default function FavoriteTable() {
  const [companies, setCompanies] = useState<TypeCompany[]>([]);
  const [openModal, setModalOpen] = useState<boolean>(false);
  const [wordToSearch, setWordToSearch] = useState<string>('');
  const [searchResults, setSearchResults] = useState<number[]>([]);

  useEffect(() => {
    const getCompanies = async () => {
      try {
        const data = await companyService.getCompanies();
        setCompanies(data.companies);
      } catch (error) {
        console.error('Failed to fetch companies:', error);
      }
    };

    getCompanies();
  }, []);

  async function handleSearchCompanies(wordToSearch: string) {
    try {
      const companiesids = await companyService.searchWordInCompany(
        wordToSearch
      );

      const foundIds = companiesids.map((id: any) => id);

      setSearchResults(foundIds);
    } catch (error) {
      console.error('Failed to fetch company details:', error);
    }
  }

  async function addJob(company: TypeCompany) {
    // await companyService.addCompany(company.company_name,company.url)
    // setCompanies([...companies, company]);
  }

  const isSearchedCompany = (company: TypeCompany) => {
    return searchResults.includes(company.id);
  };

  return (
    <>
      <Typography variant='h6' component='h2' gutterBottom>
        Favorite Companies
      </Typography>
      <TableContainer component={Paper} sx={{ maxHeight: 200 }}>
        <Table stickyHeader aria-label='companies table'>
          <TableHead>
            <TableRow>
              <TableCell style={{fontSize:18}} align='left'>
                Company
              </TableCell>
              <TableCell style={{fontSize:18}} align='left'>
                Url
              </TableCell>
              <TableCell align='right'>
                <button
                  className='company-modalButton'
                  onClick={() => setModalOpen(true)}
                >
                  AutoSearch Word
                </button>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {companies.map((company,index) => (
              <TableRow
                key={index}
                onClick={() => addJob(company)}
                sx={{
                  cursor: 'pointer',
                  backgroundColor: isSearchedCompany(company)
                    ? 'rgba(39, 243, 245, 0.48)'
                    : 'inherit',
                  transition: 'background-color 0.4s ease',
                }}
              >
                <TableCell align='left'>{company.company_name}</TableCell>
                <TableCell align='left'>
                  <a
                    href={company.url}
                    target='_blank'
                    rel='noopener noreferrer'
                  >
                    {company.url}
                  </a>
                </TableCell>
                <TableCell></TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <BasicModal
          open={openModal}
          setOpen={setModalOpen}
          children={
            <div>
              <TextField
                label='Enter Text'
                variant='outlined'
                fullWidth
                margin='normal'
                onChange={(e) => setWordToSearch(e.target.value)}
              />
              <Button
                onClick={() => {
                  handleSearchCompanies(wordToSearch);
                  setModalOpen(false);
                }}
                variant='contained'
                fullWidth
              >
                Send
              </Button>
            </div>
          }
        />
      </TableContainer>
    </>
  );
}
