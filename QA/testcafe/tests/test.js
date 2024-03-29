import { Selector } from 'testcafe';

fixture `Getting Started`
    .page `http://devexpress.github.io/testcafe/example`;

    test('My first test', async t => {
        await t
            .typeText('#developer-name', 'John Smith')
            .wait(5000)
            .click('#submit-button');

            const articleHeader = await Selector('.result-content').find('h1');

            
            // Obtain the text of the article header
            let headerText = await articleHeader.innerText;

    });

    test('My test', async t => {
        const developerNameInput = Selector('#developer-name');

        await t
            .expect(developerNameInput.value).eql('')
            .typeText(developerNameInput, 'Peter Parker')
    });

   