-- ============================
-- Insert studios
-- ============================
INSERT INTO studio (studio_name) VALUES
('David Production'),
('Bones'),
('OLM'),
('Sunrise'),
('MAPPA'),
('Production I.G'),
('Gainax'),
('Toei Animation'),
('Madhouse'),
('Wit Studio'),
('TMS Entertainment'),
('Studio Orange'),
('Liden Films'),
('A-1 Pictures'),
('Ufotable'),
('Studio Pierrot'),
('Kyoto Animation')
ON CONFLICT (studio_name) DO NOTHING;

-- ============================
-- Insert genres
-- ============================
INSERT INTO genre (name) VALUES
('Action'),
('Adventure'),
('Fantasy'),
('Drama'),
('Comedy'),
('Romance'),
('Sci-Fi'),
('Horror'),
('Mystery'),
('Thriller'),
('Psychological'),
('Supernatural')
ON CONFLICT (name) DO NOTHING;

-- ============================
-- Insert anime
-- ============================
INSERT INTO anime (title, release_year, episodes, studio_id) VALUES
('Attack on Titan', 2013, 87,
 (SELECT studio_id FROM studio WHERE studio_name='Wit Studio')),

('Jujutsu Kaisen', 2020, 47,
 (SELECT studio_id FROM studio WHERE studio_name='MAPPA')),

('Demon Slayer', 2019, 55,
 (SELECT studio_id FROM studio WHERE studio_name='Ufotable')),

('One Piece', 1999, 1100,
 (SELECT studio_id FROM studio WHERE studio_name='Toei Animation')),

('Fullmetal Alchemist: Brotherhood', 2009, 64,
 (SELECT studio_id FROM studio WHERE studio_name='Bones')),

('Death Note', 2006, 37,
 (SELECT studio_id FROM studio WHERE studio_name='Madhouse')),

('Naruto', 2002, 220,
 (SELECT studio_id FROM studio WHERE studio_name='Studio Pierrot')),

('Steins;Gate', 2011, 24,
 (SELECT studio_id FROM studio WHERE studio_name='Madhouse')),

('Violet Evergarden', 2018, 13,
 (SELECT studio_id FROM studio WHERE studio_name='Kyoto Animation')),

('Chainsaw Man', 2022, 12,
 (SELECT studio_id FROM studio WHERE studio_name='MAPPA')),

('JoJo''s Bizarre Adventure', 2012, 190,
 (SELECT studio_id FROM studio WHERE studio_name='David Production')),

('My Hero Academia', 2016, 138,
 (SELECT studio_id FROM studio WHERE studio_name='Bones')),

('Berserk', 1997, 25,
 (SELECT studio_id FROM studio WHERE studio_name='OLM')),

('Cowboy Bebop', 1998, 26,
 (SELECT studio_id FROM studio WHERE studio_name='Sunrise')),

('Fire Force', 2019, 48,
 (SELECT studio_id FROM studio WHERE studio_name='David Production')),

('Tokyo Revengers', 2021, 50,
 (SELECT studio_id FROM studio WHERE studio_name='Liden Films')),

('Neon Genesis Evangelion', 1995, 26,
 (SELECT studio_id FROM studio WHERE studio_name='Gainax')),

('Dragon Ball', 1986, 153,
 (SELECT studio_id FROM studio WHERE studio_name='Toei Animation')),

('One Punch Man', 2015, 24,
 (SELECT studio_id FROM studio WHERE studio_name='Madhouse')),

('Vinland Saga', 2019, 48,
 (SELECT studio_id FROM studio WHERE studio_name='Wit Studio')),

('Dr. Stone', 2019, 57,
 (SELECT studio_id FROM studio WHERE studio_name='TMS Entertainment')),

('Kakegurui', 2017, 24,
 (SELECT studio_id FROM studio WHERE studio_name='MAPPA')),

('Seven Deadly Sins', 2014, 100,
 (SELECT studio_id FROM studio WHERE studio_name='A-1 Pictures')),

('Beastars', 2019, 24,
 (SELECT studio_id FROM studio WHERE studio_name='Studio Orange'));

-- ============================
-- Insert anime-genre mappings
-- ============================
INSERT INTO anime_genre (anime_id, genre_id)
SELECT a.anime_id, g.genre_id
FROM anime a, genre g
WHERE
(a.title='Attack on Titan' AND g.name IN ('Action','Drama','Thriller','Mystery')) OR
(a.title='Jujutsu Kaisen' AND g.name IN ('Action','Fantasy','Adventure')) OR
(a.title='Demon Slayer' AND g.name IN ('Action','Fantasy','Adventure','Drama')) OR
(a.title='One Piece' AND g.name IN ('Action','Adventure','Comedy')) OR
(a.title='Fullmetal Alchemist: Brotherhood' AND g.name IN ('Action','Adventure','Fantasy','Drama')) OR
(a.title='Death Note' AND g.name IN ('Mystery','Thriller','Drama','Psychological')) OR
(a.title='Naruto' AND g.name IN ('Action','Adventure','Comedy')) OR
(a.title='Steins;Gate' AND g.name IN ('Sci-Fi','Mystery','Thriller')) OR
(a.title='Violet Evergarden' AND g.name IN ('Drama','Romance')) OR
(a.title='Chainsaw Man' AND g.name IN ('Action','Horror','Thriller')) OR
(a.title='JoJo''s Bizarre Adventure' AND g.name IN ('Action','Adventure','Supernatural')) OR
(a.title='My Hero Academia' AND g.name IN ('Action','Adventure','Comedy')) OR
(a.title='Berserk' AND g.name IN ('Action','Drama','Fantasy')) OR
(a.title='Cowboy Bebop' AND g.name IN ('Action','Sci-Fi')) OR
(a.title='Fire Force' AND g.name IN ('Action','Supernatural')) OR
(a.title='Tokyo Revengers' AND g.name IN ('Action','Drama')) OR
(a.title='Neon Genesis Evangelion' AND g.name IN ('Sci-Fi','Drama','Psychological')) OR
(a.title='Dragon Ball' AND g.name IN ('Action','Adventure','Fantasy')) OR
(a.title='One Punch Man' AND g.name IN ('Action','Comedy')) OR
(a.title='Vinland Saga' AND g.name IN ('Action','Drama')) OR
(a.title='Dr. Stone' AND g.name IN ('Sci-Fi','Adventure')) OR
(a.title='Kakegurui' AND g.name IN ('Drama','Psychological','Thriller')) OR
(a.title='Seven Deadly Sins' AND g.name IN ('Action','Adventure','Fantasy')) OR
(a.title='Beastars' AND g.name IN ('Drama','Psychological'));
