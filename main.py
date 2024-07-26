import layoutManager
import Alg

PDFs = ['The Grammar of English Grammars.pdf', 'Chubby--Charming.pdf', 'Harry Potter and the Cursed Child.pdf', 'The Book Thief.pdf', 'The Hitchhikers Guide to the Galaxy.pdf', 'The Last Crusade.pdf']
test = ['meetingminutes.pdf']
layoutManager.getGraph(PDFs)
Alg.minimize()